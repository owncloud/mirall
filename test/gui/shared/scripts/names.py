# encoding: UTF-8

from objectmaphelper import *

settings_OCC_SettingsDialog = {"name": "Settings", "type": "OCC::SettingsDialog", "visible": 1}
settings_settingsdialog_toolbutton_Add_account_QToolButton = {"name": "settingsdialog_toolbutton_Add account", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
owncloudWizard_OCC_OwncloudWizard = {"name": "owncloudWizard", "type": "OCC::OwncloudWizard", "visible": 1}
owncloudWizard_label_2_QLabel = {"name": "label_2", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
leUrl_OCC_PostfixLineEdit = {"buddy": owncloudWizard_label_2_QLabel, "name": "leUrl", "type": "OCC::PostfixLineEdit", "visible": 1}
owncloudWizard_qt_passive_wizardbutton1_QPushButton = {"name": "__qt__passive_wizardbutton1", "type": "QPushButton", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
owncloudWizard_lLocal_QLabel = {"name": "lLocal", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
pbSelectLocalFolder_QPushButton = {"buddy": owncloudWizard_lLocal_QLabel, "name": "pbSelectLocalFolder", "type": "QPushButton", "visible": 1}
qFileDialog_QFileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
qFileDialog_splitter_QSplitter = {"name": "splitter", "type": "QSplitter", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_frame_QFrame = {"container": qFileDialog_splitter_QSplitter, "name": "frame", "type": "QFrame", "visible": 1}
frame_stackedWidget_QStackedWidget = {"container": splitter_frame_QFrame, "name": "stackedWidget", "type": "QStackedWidget", "visible": 1}
stackedWidget_treeView_QTreeView = {"container": frame_stackedWidget_QStackedWidget, "name": "treeView", "type": "QTreeView", "visible": 1}
qFileDialog_newFolderButton_QToolButton = {"name": "newFolderButton", "type": "QToolButton", "visible": 1, "window": qFileDialog_QFileDialog}
treeView_QExpandingLineEdit = {"columnIndex": 0, "container": stackedWidget_treeView_QTreeView, "rowIndex": 2, "type": "QExpandingLineEdit", "unnamed": 1, "visible": 1}
qFileDialog_Choose_QPushButton = {"text": "Choose", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": qFileDialog_QFileDialog}
enter_Password_QInputDialog = {"type": "QInputDialog", "unnamed": 1, "visible": 1, "windowTitle": "Enter Password"}
enter_Password_Cancel_QPushButton = {"text": "Cancel", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": enter_Password_QInputDialog}
settings_settingsdialog_toolbutton_admin_localhost_QToolButton = {"name": "settingsdialog_toolbutton_admin@localhost", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
settings_stack_QStackedWidget = {"name": "stack", "type": "QStackedWidget", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_accountToolbox_QToolButton = {"container": settings_stack_QStackedWidget, "name": "_accountToolbox", "type": "QToolButton", "visible": 1}
settings_QMenu = {"type": "QMenu", "unnamed": 1, "visible": 1, "window": settings_OCC_SettingsDialog}
stack_Remove_connection_QPushButton = {"container": settings_stack_QStackedWidget, "text": "Remove connection", "type": "QPushButton", "unnamed": 1, "visible": 1}
owncloudWizard_usernameLabel_QLabel = {"name": "usernameLabel", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
leUsername_QLineEdit = {"buddy": owncloudWizard_usernameLabel_QLabel, "name": "leUsername", "type": "QLineEdit", "visible": 1}
owncloudWizard_passwordLabel_QLabel = {"name": "passwordLabel", "type": "QLabel", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
lePassword_QLineEdit = {"buddy": owncloudWizard_passwordLabel_QLabel, "name": "lePassword", "type": "QLineEdit", "visible": 1}
qFileDialog_fileNameLabel_QLabel = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": qFileDialog_QFileDialog}
fileNameEdit_QLineEdit = {"buddy": qFileDialog_fileNameLabel_QLabel, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
owncloudWizard_cbSyncFromScratch_QRadioButton = {"name": "cbSyncFromScratch", "type": "QRadioButton", "visible": 1, "window": owncloudWizard_OCC_OwncloudWizard}
settings_settingsdialog_toolbutton_artur_jankaritech_ocloud_de_QToolButton = {"name": "settingsdialog_toolbutton_artur@jankaritech.ocloud.de", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_folderList_QTreeView = {"container": settings_stack_QStackedWidget, "name": "_folderList", "type": "QTreeView", "visible": 1}
sharingDialog_OCC_ShareDialog = {"name": "SharingDialog", "type": "OCC::ShareDialog", "visible": 1}
sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget = {"name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
qt_tabwidget_stackedwidget_SharingDialogUG_OCC_ShareUserGroupWidget = {"container": sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget, "name": "SharingDialogUG", "type": "OCC::ShareUserGroupWidget", "visible": 1}
sharingDialogUG_shareeLineEdit_QLineEdit = {"container": qt_tabwidget_stackedwidget_SharingDialogUG_OCC_ShareUserGroupWidget, "name": "shareeLineEdit", "type": "QLineEdit", "visible": 1}
o_QListView = {"type": "QListView", "unnamed": 1, "visible": 1}
sharingDialogUG_scrollArea_QScrollArea = {"container": qt_tabwidget_stackedwidget_SharingDialogUG_OCC_ShareUserGroupWidget, "name": "scrollArea", "type": "QScrollArea", "visible": 1}
scrollArea_deleteShareButton_QToolButton = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "deleteShareButton", "type": "QToolButton", "visible": 1}
sharingDialog_Close_QPushButton = {"text": "Close", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": sharingDialog_OCC_ShareDialog}
settings_settingsdialog_toolbutton_Quit_ownCloud_QToolButton = {"name": "settingsdialog_toolbutton_Quit ownCloud", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
quit_ownCloud_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Quit ownCloud"}
quit_ownCloud_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": quit_ownCloud_QMessageBox}
qFileDialog_lookInCombo_QComboBox = {"name": "lookInCombo", "type": "QComboBox", "visible": 1, "window": qFileDialog_QFileDialog}
splitter_sidebar_QSidebar = {"container": qFileDialog_splitter_QSplitter, "name": "sidebar", "type": "QSidebar", "visible": 1}
settings_settingsdialog_toolbutton_Settings_QToolButton = {"name": "settingsdialog_toolbutton_Settings", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_scrollArea_QScrollArea = {"container": settings_stack_QStackedWidget, "name": "scrollArea", "type": "QScrollArea", "visible": 1}
scrollArea_QScrollBar = {"container": stack_scrollArea_QScrollArea, "type": "QScrollBar", "unnamed": 1, "visible": 1}
scrollArea_groupBox_QGroupBox = {"container": stack_scrollArea_QScrollArea, "name": "groupBox", "type": "QGroupBox", "visible": 1}
groupBox_proxyGroupBox_QGroupBox = {"container": scrollArea_groupBox_QGroupBox, "name": "proxyGroupBox", "type": "QGroupBox", "visible": 1}
proxyGroupBox_manualProxyRadioButton_QRadioButton = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "manualProxyRadioButton", "type": "QRadioButton", "visible": 1}
proxyGroupBox_hostLineEdit_QLineEdit = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "hostLineEdit", "type": "QLineEdit", "visible": 1}
proxyGroupBox_authRequiredcheckBox_QCheckBox = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "authRequiredcheckBox", "type": "QCheckBox", "visible": 1}
proxyGroupBox_labelLocalhost_QLabel = {"container": groupBox_proxyGroupBox_QGroupBox, "name": "labelLocalhost", "type": "QLabel", "visible": 1}
groupBox_uploadBox_QGroupBox = {"container": scrollArea_groupBox_QGroupBox, "name": "uploadBox", "type": "QGroupBox", "visible": 1}
uploadBox_autoUploadLimitRadioButton_QRadioButton = {"container": groupBox_uploadBox_QGroupBox, "name": "autoUploadLimitRadioButton", "type": "QRadioButton", "visible": 1}
settings_settingsdialog_toolbutton_Activity_QToolButton = {"name": "settingsdialog_toolbutton_Activity", "type": "QToolButton", "visible": 1, "window": settings_OCC_SettingsDialog}
stack_qt_tabwidget_stackedwidget_QStackedWidget = {"container": settings_stack_QStackedWidget, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ActivityWidget", "type": "OCC::ActivityWidget", "visible": 1}
oCC_ActivityWidget_activityList_QListView = {"container": qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget, "name": "_activityList", "type": "QListView", "visible": 1}
o_activityList_QScrollBar = {"container": oCC_ActivityWidget_activityList_QListView, "type": "QScrollBar", "unnamed": 1, "visible": 1}
oCC_ActivityWidget_notifyScroll_QScrollArea = {"container": qt_tabwidget_stackedwidget_OCC_ActivityWidget_OCC_ActivityWidget, "name": "_notifyScroll", "type": "QScrollArea", "visible": 1}
o_notifyScroll_QScrollBar = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "type": "QScrollBar", "unnamed": 1, "visible": 1}
o_notifyScroll_Accept_QPushButton = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "text": "Accept", "type": "QPushButton", "unnamed": 1, "visible": 1}
o_notifyScroll_timeLabel_QLabel = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "name": "_timeLabel", "type": "QLabel", "visible": 1}
o_notifyScroll_subjectLabel_QLabel = {"container": oCC_ActivityWidget_notifyScroll_QScrollArea, "name": "_subjectLabel", "type": "QLabel", "visible": 1}
scrollArea_OCC_ShareUserLine_OCC_ShareUserLine = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "OCC__ShareUserLine", "type": "OCC::ShareUserLine", "visible": 1}
scrollArea_permissionShare_QCheckBox = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "permissionShare", "type": "QCheckBox", "visible": 1}
scrollArea_permissionsEdit_QCheckBox = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "permissionsEdit", "type": "QCheckBox", "visible": 1}
scrollArea_sharedWith_QLabel = {"container": sharingDialogUG_scrollArea_QScrollArea, "name": "sharedWith", "type": "QLabel", "visible": 1}
enter_Password_Field = {"container": enter_Password_QInputDialog, "type": "QLineEdit", "unnamed": 1, "visible": 1}
enter_Password_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": enter_Password_QInputDialog}
o_folderList_QModelIndex = {"column": 0, "container": stack_folderList_QTreeView, "text": "", "type": "QModelIndex"}
qt_tabwidget_stackedwidget_OCC_IssuesWidget_OCC_IssuesWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__IssuesWidget", "type": "OCC::IssuesWidget", "visible": 1}
oCC_IssuesWidget_treeWidget_QTreeWidget = {"container": qt_tabwidget_stackedwidget_OCC_IssuesWidget_OCC_IssuesWidget, "name": "_treeWidget", "type": "QTreeWidget", "visible": 1}
o_treeWidget_lorem_conflicted_copy_2020_12_14_133239_txt_QModelIndex = {"column": 1, "container": oCC_IssuesWidget_treeWidget_QTreeWidget, "text": RegularExpression("lorem (conflicted copy 2020-12-14 133239).txt"), "type": "QModelIndex"}
stack_QTabWidget = {"container": settings_stack_QStackedWidget, "type": "QTabWidget", "unnamed": 1, "visible": 1}
stack_qt_tabwidget_tabbar_QTabBar = {"container": settings_stack_QStackedWidget, "name": "qt_tabwidget_tabbar", "type": "QTabBar", "visible": 1}
o_treeWidget_Conflict_Server_version_downloaded_local_copy_renamed_and_not_uploaded_QModelIndex = {"column": 3, "container": oCC_IssuesWidget_treeWidget_QTreeWidget, "text": "Conflict: Server version downloaded, local copy renamed and not uploaded.", "type": "QModelIndex"}
qt_tabwidget_stackedwidget_OCC_ProtocolWidget_OCC_ProtocolWidget = {"container": stack_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ProtocolWidget", "type": "OCC::ProtocolWidget", "visible": 1}
oCC_ProtocolWidget_treeWidget_QTreeWidget = {"container": qt_tabwidget_stackedwidget_OCC_ProtocolWidget_OCC_ProtocolWidget, "name": "_treeWidget", "type": "QTreeWidget", "visible": 1}
o_treeWidget_lorem_txt_QModelIndex = {"column": 1, "container": oCC_ProtocolWidget_treeWidget_QTreeWidget, "text": "lorem.txt", "type": "QModelIndex"}
sharingDialog_qt_tabwidget_tabbar_QTabBar = {"name": "qt_tabwidget_tabbar", "type": "QTabBar", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
qt_tabwidget_tabbar_Public_Links_TabItem = {"container": sharingDialog_qt_tabwidget_tabbar_QTabBar, "text": "Public Links", "type": "TabItem"}
qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget = {"container": sharingDialog_qt_tabwidget_stackedwidget_QStackedWidget, "name": "OCC__ShareLinkWidget", "type": "OCC::ShareLinkWidget", "visible": 1}
oCC_ShareLinkWidget_checkBox_password_QCheckBox = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "checkBox_password", "type": "QCheckBox", "visible": 1}
oCC_ShareLinkWidget_widget_editing_QWidget = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "widget_editing", "type": "QWidget", "visible": 1}
oCC_ShareLinkWidget_checkBox_password_QProgressIndicator = {"aboveWidget": oCC_ShareLinkWidget_widget_editing_QWidget, "container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "leftWidget": oCC_ShareLinkWidget_checkBox_password_QCheckBox, "type": "QProgressIndicator", "unnamed": 1, "visible": 1}
sharingDialog_The_file_can_not_be_shared_because_it_was_shared_without_sharing_permission_QLabel = {"text": "The file can not be shared because it was shared without sharing permission.", "type": "QLabel", "unnamed": 1, "visible": 1, "window": sharingDialog_OCC_ShareDialog}
sharingDialog_label_name_QLabel = {"name": "label_name", "type": "QLabel", "visible": 1, "window": sharingDialog_OCC_ShareDialog}
oCC_ShareLinkWidget_createShareButton_QPushButton = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "createShareButton", "type": "QPushButton", "visible": 1}
oCC_ShareLinkWidget_linkShares_QTableWidget = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "linkShares", "type": "QTableWidget", "visible": 1}
linkShares_QToolButton = {"container": oCC_ShareLinkWidget_linkShares_QTableWidget, "text": "...", "type": "QToolButton", "unnamed": 1, "visible": 1}
oCC_ShareLinkWidget_lineEdit_password_QLineEdit = {"container": qt_tabwidget_stackedwidget_OCC_ShareLinkWidget_OCC_ShareLinkWidget, "name": "lineEdit_password", "type": "QLineEdit", "visible": 1}