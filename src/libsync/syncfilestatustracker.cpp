/*
 * Copyright (C) by Klaas Freitag <freitag@owncloud.com>
 * Copyright (C) by Jocelyn Turcotte <jturcotte@woboq.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
 * for more details.
 */

#include "syncfilestatustracker.h"
#include "syncengine.h"
#include "syncjournaldb.h"
#include "syncjournalfilerecord.h"

namespace OCC {

static SyncFileStatus::SyncFileStatusTag lookupProblem(const QString &pathToMatch, const std::map<QString, SyncFileStatus::SyncFileStatusTag> &problemMap)
{
    auto lower = problemMap.lower_bound(pathToMatch);
    for (auto it = lower; it != problemMap.cend(); ++it) {
        const QString &problemPath = it->first;
        SyncFileStatus::SyncFileStatusTag severity = it->second;
        // qDebug() << Q_FUNC_INFO << pathToMatch << severity << problemPath;
        if (problemPath == pathToMatch) {
            return severity;
        } else if (severity == SyncFileStatus::StatusError
                && problemPath.startsWith(pathToMatch)
                && (pathToMatch.isEmpty() || problemPath.at(pathToMatch.size()) == '/')) {
            return SyncFileStatus::StatusWarning;
        } else if (!problemPath.startsWith(pathToMatch)) {
            // Starting at lower_bound we get the first path that is not smaller,
            // since: "a/" < "a/aa" < "a/aa/aaa" < "a/ab/aba"
            // If problemMap keys are ["a/aa/aaa", "a/ab/aba"] and pathToMatch == "a/aa",
            // lower_bound(pathToMatch) will point to "a/aa/aaa", and the moment that
            // problemPath.startsWith(pathToMatch) == false, we know that we've looked
            // at everything that interest us.
            break;
        }
    }
    return SyncFileStatus::StatusNone;
}

/**
 * Whether this item should get an ERROR icon through the Socket API.
 *
 * The Socket API should only present serious, permanent errors to the user.
 * In particular SoftErrors should just retain their 'needs to be synced'
 * icon as the problem is most likely going to resolve itself quickly and
 * automatically.
 */
static inline bool showErrorInSocketApi(const SyncFileItem& item)
{
    const auto status = item._status;
    return item._instruction == CSYNC_INSTRUCTION_ERROR
        || status == SyncFileItem::NormalError
        || status == SyncFileItem::FatalError
        || item._hasBlacklistEntry;
}

static inline bool showWarningInSocketApi(const SyncFileItem& item)
{
    const auto status = item._status;
    return item._instruction == CSYNC_INSTRUCTION_IGNORE
        || status == SyncFileItem::FileIgnored
        || status == SyncFileItem::Conflict
        || status == SyncFileItem::Restoration;
}

SyncFileStatusTracker::SyncFileStatusTracker(SyncEngine *syncEngine)
    : _syncEngine(syncEngine)
{
    connect(syncEngine, SIGNAL(aboutToPropagate(SyncFileItemVector&)),
            SLOT(slotAboutToPropagate(SyncFileItemVector&)));
    connect(syncEngine, SIGNAL(itemCompleted(const SyncFileItem&, const PropagatorJob&)),
            SLOT(slotItemCompleted(const SyncFileItem&)));
    connect(syncEngine, SIGNAL(started()), SLOT(slotSyncEngineRunningChanged()));
    connect(syncEngine, SIGNAL(finished(bool)), SLOT(slotSyncEngineRunningChanged()));
}

SyncFileStatus SyncFileStatusTracker::fileStatus(const QString& relativePath)
{
    Q_ASSERT(!relativePath.endsWith(QLatin1Char('/')));

    if (relativePath.isEmpty()) {
        // This is the root sync folder, it doesn't have an entry in the database and won't be walked by csync, so resolve manually.
        return resolveSyncAndErrorStatus(QString(), NotShared);
    }

    // The SyncEngine won't notify us at all for CSYNC_FILE_SILENTLY_EXCLUDED
    // and CSYNC_FILE_EXCLUDE_AND_REMOVE excludes. Even though it's possible
    // that the status of CSYNC_FILE_EXCLUDE_LIST excludes will change if the user
    // update the exclude list at runtime and doing it statically here removes
    // our ability to notify changes through the fileStatusChanged signal,
    // it's an acceptable compromize to treat all exclude types the same.
    if( _syncEngine->excludedFiles().isExcluded(_syncEngine->localPath() + relativePath,
                                                _syncEngine->localPath(),
                                                _syncEngine->ignoreHiddenFiles()) ) {
        return SyncFileStatus(SyncFileStatus::StatusWarning);
    }

    if ( _dirtyPaths.contains(relativePath) )
        return SyncFileStatus::StatusSync;

    // First look it up in the database to know if it's shared
    SyncJournalFileRecord rec = _syncEngine->journal()->getFileRecord(relativePath);
    if (rec.isValid()) {
        return resolveSyncAndErrorStatus(relativePath, rec._remotePerm.contains("S") ? Shared : NotShared);
    }

    // Must be a new file not yet in the database, check if it's syncing or has an error.
    return resolveSyncAndErrorStatus(relativePath, NotShared, PathUnknown);
}

void SyncFileStatusTracker::slotPathTouched(const QString& fileName)
{
    QString folderPath = _syncEngine->localPath();
    Q_ASSERT(fileName.startsWith(folderPath));

    QString localPath = fileName.mid(folderPath.size());
    _dirtyPaths.insert(localPath);

    emit fileStatusChanged(fileName, SyncFileStatus::StatusSync);
}

void SyncFileStatusTracker::incSyncCount(const QString &relativePath, EmitStatusChangeFlag emitStatusChange)
{
    // Will return 0 (and increase to 1) if the path wasn't in the map yet
    int count = _syncCount[relativePath]++;
    if (!count) {
        if (emitStatusChange)
            emit fileStatusChanged(getSystemDestination(relativePath), fileStatus(relativePath));

        // We passed from OK to SYNC, increment the parent to keep it marked as
        // SYNC while we propagate ourselves and our own children.
        Q_ASSERT(!relativePath.endsWith('/'));
        int lastSlashIndex = relativePath.lastIndexOf('/');
        if (lastSlashIndex != -1)
            incSyncCount(relativePath.left(lastSlashIndex), EmitStatusChange);
        else if (!relativePath.isEmpty())
            incSyncCount(QString(), EmitStatusChange);
    }
}

void SyncFileStatusTracker::decSyncCount(const QString &relativePath, EmitStatusChangeFlag emitStatusChange)
{
    int count = --_syncCount[relativePath];
    if (!count) {
        // Remove from the map, same as 0
        _syncCount.remove(relativePath);

        if (emitStatusChange)
            emit fileStatusChanged(getSystemDestination(relativePath), fileStatus(relativePath));

        // We passed from SYNC to OK, decrement our parent.
        Q_ASSERT(!relativePath.endsWith('/'));
        int lastSlashIndex = relativePath.lastIndexOf('/');
        if (lastSlashIndex != -1)
            decSyncCount(relativePath.left(lastSlashIndex), EmitStatusChange);
        else if (!relativePath.isEmpty())
            decSyncCount(QString(), EmitStatusChange);
    }
}

void SyncFileStatusTracker::slotAboutToPropagate(SyncFileItemVector& items)
{
    // New sync, clear the sync counts to reduce the impact of a bug that would cause unsymetrical inc/dec
    Q_ASSERT(_syncCount.isEmpty());
    _syncCount.clear();

    std::map<QString, SyncFileStatus::SyncFileStatusTag> oldProblems;
    std::swap(_syncProblems, oldProblems);

    foreach (const SyncFileItemPtr &item, items) {
        // qDebug() << Q_FUNC_INFO << "Investigating" << item->destination() << item->_status << item->_instruction;

        if (showErrorInSocketApi(*item)) {
            _syncProblems[item->_file] = SyncFileStatus::StatusError;
            invalidateParentPaths(item->destination());
        } else if (showWarningInSocketApi(*item)) {
            _syncProblems[item->_file] = SyncFileStatus::StatusWarning;
        }

        // Mark this path as syncing for instructions that will result in propagation,
        // but DontEmitStatusChange since we're going to emit for ourselves using the
        // info in the SyncFileItem we received, parents will still be emit if needed.
        if (item->_instruction != CSYNC_INSTRUCTION_NONE
            && item->_instruction != CSYNC_INSTRUCTION_UPDATE_METADATA
            && item->_instruction != CSYNC_INSTRUCTION_IGNORE
            && item->_instruction != CSYNC_INSTRUCTION_ERROR) {
            incSyncCount(item->destination(), DontEmitStatusChange);
        }

        _dirtyPaths.remove(item->destination());
        emit fileStatusChanged(getSystemDestination(item->destination()), resolveSyncAndErrorStatus(item->destination(), item->_remotePerm.contains("S") ? Shared : NotShared));
    }

    // Some metadata status won't trigger files to be synced, make sure that we
    // push the OK status for dirty files that don't need to be propagated.
    // Swap into a copy since fileStatus() reads _dirtyPaths to determine the status
    QSet<QString> oldDirtyPaths;
    std::swap(_dirtyPaths, oldDirtyPaths);
    for (auto it = oldDirtyPaths.constBegin(); it != oldDirtyPaths.constEnd(); ++it)
        emit fileStatusChanged(getSystemDestination(*it), fileStatus(*it));

    // Make sure to push any status that might have been resolved indirectly since the last sync
    // (like an error file being deleted from disk)
    for (auto it = _syncProblems.begin(); it != _syncProblems.end(); ++it)
        oldProblems.erase(it->first);
    for (auto it = oldProblems.begin(); it != oldProblems.end(); ++it) {
        const QString &path = it->first;
        SyncFileStatus::SyncFileStatusTag severity = it->second;
        if (severity == SyncFileStatus::StatusError)
            invalidateParentPaths(path);
        emit fileStatusChanged(getSystemDestination(path), fileStatus(path));
    }
}

void SyncFileStatusTracker::slotItemCompleted(const SyncFileItem &item)
{
    // qDebug() << Q_FUNC_INFO << item.destination() << item._status << item._instruction;

    if (showErrorInSocketApi(item)) {
        _syncProblems[item._file] = SyncFileStatus::StatusError;
        invalidateParentPaths(item.destination());
    } else if (showWarningInSocketApi(item)) {
        _syncProblems[item._file] = SyncFileStatus::StatusWarning;
    } else {
        _syncProblems.erase(item._file);
    }

    // decSyncCount calls *must* be symetric with incSyncCount calls in slotAboutToPropagate
    if (item._instruction != CSYNC_INSTRUCTION_NONE
        && item._instruction != CSYNC_INSTRUCTION_UPDATE_METADATA
        && item._instruction != CSYNC_INSTRUCTION_IGNORE
        && item._instruction != CSYNC_INSTRUCTION_ERROR) {
        decSyncCount(item.destination(), DontEmitStatusChange);
    }
    emit fileStatusChanged(getSystemDestination(item.destination()), resolveSyncAndErrorStatus(item.destination(), item._remotePerm.contains("S") ? Shared : NotShared));
}

void SyncFileStatusTracker::slotSyncEngineRunningChanged()
{
    emit fileStatusChanged(_syncEngine->localPath(), resolveSyncAndErrorStatus(QString(), NotShared));
}

SyncFileStatus SyncFileStatusTracker::resolveSyncAndErrorStatus(const QString &relativePath, SharedFlag isShared, PathKnownFlag isPathKnown)
{
    // If it's a new file and that we're not syncing it yet,
    // don't show any icon and wait for the filesystem watcher to trigger a sync.
    SyncFileStatus status(isPathKnown ? SyncFileStatus::StatusUpToDate : SyncFileStatus::StatusNone);
    if (_syncCount.value(relativePath)) {
        status.set(SyncFileStatus::StatusSync);
    } else {
        // After a sync finished, we need to show the users issues from that last sync like the activity list does.
        // Also used for parent directories showing a warning for an error child.
        SyncFileStatus::SyncFileStatusTag problemStatus = lookupProblem(relativePath, _syncProblems);
        if (problemStatus != SyncFileStatus::StatusNone)
            status.set(problemStatus);
    }

    if (isShared)
        status.setSharedWithMe(true);

    return status;
}

void SyncFileStatusTracker::invalidateParentPaths(const QString& path)
{
    QStringList splitPath = path.split('/', QString::SkipEmptyParts);
    for (int i = 0; i < splitPath.size(); ++i) {
        QString parentPath = QStringList(splitPath.mid(0, i)).join(QLatin1String("/"));
        emit fileStatusChanged(getSystemDestination(parentPath), fileStatus(parentPath));
    }
}

QString SyncFileStatusTracker::getSystemDestination(const QString& relativePath)
{
    QString systemPath = _syncEngine->localPath() + relativePath;
    // SyncEngine::localPath() has a trailing slash, make sure to remove it if the
    // destination is empty.
    if( systemPath.endsWith(QLatin1Char('/')) ) {
        systemPath.truncate(systemPath.length()-1);
    }
    return systemPath;
}

}
