/*
 * Copyright (C) by Daniel Molkentin <danimo@owncloud.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
 * for more details.
 */

#include "cocoainitializer.h"

#import <Foundation/NSAutoreleasePool.h>
#import <AppKit/NSApplication.h>

#include <QDebug>
#include <QMessageBox>

@interface OwnAppDelegate : NSObject<NSApplicationDelegate>
- (BOOL)applicationShouldHandleReopen:(NSApplication *)sender hasVisibleWindows:(BOOL)flag;
@end

@implementation OwnAppDelegate {
}

- (BOOL)applicationShouldHandleReopen:(NSApplication *)sender hasVisibleWindows:(BOOL)flag
{
    qDebug() << "HERE!";
  QMessageBox::information(nullptr, "OwnAppDelegate", QStringLiteral("Yo yo, received a message named: applicationShouldHandleReopen, hasVisibleWindows:%1").arg(flag?"YES":"NO"));
  return YES;
}

@end

namespace OCC {
namespace Mac {

class CocoaInitializer::Private {
  public:
    NSAutoreleasePool* autoReleasePool;
    OwnAppDelegate *appDelegate;
};

CocoaInitializer::CocoaInitializer() {
  d = new CocoaInitializer::Private();
  NSApplicationLoad();
  d->autoReleasePool = [[NSAutoreleasePool alloc] init];
  d->appDelegate = [[OwnAppDelegate alloc] init];
  [[NSApplication sharedApplication] setDelegate:d->appDelegate];
}

CocoaInitializer::~CocoaInitializer() {
  [d->appDelegate release];
  [d->autoReleasePool release];
  delete d;
}

} // namespace Mac
} // namespace OCC
