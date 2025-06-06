# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uaclient/mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 879)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("uaclient/../network.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 922, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuOPC_UA_Client = QtWidgets.QMenu(self.menuBar)
        self.menuOPC_UA_Client.setObjectName("menuOPC_UA_Client")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.attrDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attrDockWidget.sizePolicy().hasHeightForWidth())
        self.attrDockWidget.setSizePolicy(sizePolicy)
        self.attrDockWidget.setMinimumSize(QtCore.QSize(400, 170))
        self.attrDockWidget.setObjectName("attrDockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(100, 0))
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.attrView = QtWidgets.QTreeView(self.dockWidgetContents)
        self.attrView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.attrView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.attrView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.attrView.setProperty("showDropIndicator", False)
        self.attrView.setTextElideMode(QtCore.Qt.ElideNone)
        self.attrView.setAutoExpandDelay(-1)
        self.attrView.setIndentation(18)
        self.attrView.setSortingEnabled(True)
        self.attrView.setWordWrap(True)
        self.attrView.setObjectName("attrView")
        self.gridLayout_4.addWidget(self.attrView, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.attrRefreshButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.attrRefreshButton.setObjectName("attrRefreshButton")
        self.gridLayout_4.addWidget(self.attrRefreshButton, 1, 1, 1, 1)
        self.attrDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.attrDockWidget)
        self.addrDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addrDockWidget.sizePolicy().hasHeightForWidth())
        self.addrDockWidget.setSizePolicy(sizePolicy)
        self.addrDockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.addrDockWidget.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.addrDockWidget.setObjectName("addrDockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.connectButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.connectButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 1, 4, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.disconnectButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 1, 5, 1, 1)
        self.addrComboBox = QtWidgets.QComboBox(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addrComboBox.sizePolicy().hasHeightForWidth())
        self.addrComboBox.setSizePolicy(sizePolicy)
        self.addrComboBox.setEditable(True)
        self.addrComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.addrComboBox.setObjectName("addrComboBox")
        self.gridLayout.addWidget(self.addrComboBox, 1, 2, 1, 1)
        self.connectOptionButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.connectOptionButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.connectOptionButton.setObjectName("connectOptionButton")
        self.gridLayout.addWidget(self.connectOptionButton, 1, 3, 1, 1)
        self.addrDockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.addrDockWidget)
        self.subDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subDockWidget.sizePolicy().hasHeightForWidth())
        self.subDockWidget.setSizePolicy(sizePolicy)
        self.subDockWidget.setObjectName("subDockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.subView = QtWidgets.QTableView(self.dockWidgetContents_3)
        self.subView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.subView.setAcceptDrops(True)
        self.subView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.subView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.subView.setTabKeyNavigation(False)
        self.subView.setDragDropOverwriteMode(False)
        self.subView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.subView.setObjectName("subView")
        self.gridLayout_3.addWidget(self.subView, 0, 0, 1, 1)
        self.subDockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.subDockWidget)
        self.refDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refDockWidget.sizePolicy().hasHeightForWidth())
        self.refDockWidget.setSizePolicy(sizePolicy)
        self.refDockWidget.setObjectName("refDockWidget")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.refView = QtWidgets.QTableView(self.dockWidgetContents_4)
        self.refView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.refView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.refView.setTabKeyNavigation(False)
        self.refView.setObjectName("refView")
        self.verticalLayout_2.addWidget(self.refView)
        self.refDockWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.refDockWidget)
        self.evDockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evDockWidget.sizePolicy().hasHeightForWidth())
        self.evDockWidget.setSizePolicy(sizePolicy)
        self.evDockWidget.setObjectName("evDockWidget")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.evView = QtWidgets.QListView(self.dockWidgetContents_5)
        self.evView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.evView.setAcceptDrops(True)
        self.evView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.evView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.evView.setObjectName("evView")
        self.gridLayout_5.addWidget(self.evView, 0, 0, 1, 1)
        self.evDockWidget.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.evDockWidget)
        self.logDockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.logDockWidget_2.setObjectName("logDockWidget_2")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.logTextEdit = QtWidgets.QTextEdit(self.dockWidgetContents_7)
        self.logTextEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.logTextEdit.setTabChangesFocus(True)
        self.logTextEdit.setReadOnly(False)
        self.logTextEdit.setObjectName("logTextEdit")
        self.gridLayout_6.addWidget(self.logTextEdit, 0, 0, 1, 1)
        self.logDockWidget_2.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.logDockWidget_2)
        self.graphDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.graphDockWidget.setObjectName("graphDockWidget")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphLayout = QtWidgets.QVBoxLayout()
        self.graphLayout.setSpacing(6)
        self.graphLayout.setObjectName("graphLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNumberOfPoints = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.labelNumberOfPoints.setObjectName("labelNumberOfPoints")
        self.horizontalLayout.addWidget(self.labelNumberOfPoints)
        self.spinBoxNumberOfPoints = QtWidgets.QSpinBox(self.dockWidgetContents_6)
        self.spinBoxNumberOfPoints.setMinimum(10)
        self.spinBoxNumberOfPoints.setMaximum(100)
        self.spinBoxNumberOfPoints.setProperty("value", 30)
        self.spinBoxNumberOfPoints.setObjectName("spinBoxNumberOfPoints")
        self.horizontalLayout.addWidget(self.spinBoxNumberOfPoints)
        self.labelIntervall = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.labelIntervall.setObjectName("labelIntervall")
        self.horizontalLayout.addWidget(self.labelIntervall)
        self.spinBoxIntervall = QtWidgets.QSpinBox(self.dockWidgetContents_6)
        self.spinBoxIntervall.setMinimum(1)
        self.spinBoxIntervall.setMaximum(3600)
        self.spinBoxIntervall.setProperty("value", 5)
        self.spinBoxIntervall.setObjectName("spinBoxIntervall")
        self.horizontalLayout.addWidget(self.spinBoxIntervall)
        self.buttonApply = QtWidgets.QPushButton(self.dockWidgetContents_6)
        self.buttonApply.setObjectName("buttonApply")
        self.horizontalLayout.addWidget(self.buttonApply)
        self.graphLayout.addLayout(self.horizontalLayout)
        self.gridLayout_7.addLayout(self.graphLayout, 0, 0, 1, 1)
        self.graphDockWidget.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.graphDockWidget)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionSubscribeDataChange = QtWidgets.QAction(MainWindow)
        self.actionSubscribeDataChange.setObjectName("actionSubscribeDataChange")
        self.actionUnsubscribeDataChange = QtWidgets.QAction(MainWindow)
        self.actionUnsubscribeDataChange.setObjectName("actionUnsubscribeDataChange")
        self.actionSubscribeEvent = QtWidgets.QAction(MainWindow)
        self.actionSubscribeEvent.setObjectName("actionSubscribeEvent")
        self.actionUnsubscribeEvents = QtWidgets.QAction(MainWindow)
        self.actionUnsubscribeEvents.setObjectName("actionUnsubscribeEvents")
        self.actionCopyPath = QtWidgets.QAction(MainWindow)
        self.actionCopyPath.setObjectName("actionCopyPath")
        self.actionCopyNodeId = QtWidgets.QAction(MainWindow)
        self.actionCopyNodeId.setObjectName("actionCopyNodeId")
        self.actionAddToGraph = QtWidgets.QAction(MainWindow)
        self.actionAddToGraph.setObjectName("actionAddToGraph")
        self.actionRemoveFromGraph = QtWidgets.QAction(MainWindow)
        self.actionRemoveFromGraph.setObjectName("actionRemoveFromGraph")
        self.actionCall = QtWidgets.QAction(MainWindow)
        self.actionCall.setObjectName("actionCall")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionClient_Application_Certificate = QtWidgets.QAction(MainWindow)
        self.actionClient_Application_Certificate.setObjectName("actionClient_Application_Certificate")
        self.actionFocusTree = QtWidgets.QAction(MainWindow)
        self.actionFocusTree.setObjectName("actionFocusTree")
        self.menuOPC_UA_Client.addAction(self.actionConnect)
        self.menuOPC_UA_Client.addAction(self.actionDisconnect)
        self.menuOPC_UA_Client.addAction(self.actionCopyPath)
        self.menuOPC_UA_Client.addAction(self.actionCopyNodeId)
        self.menuOPC_UA_Client.addAction(self.actionSubscribeDataChange)
        self.menuOPC_UA_Client.addAction(self.actionUnsubscribeDataChange)
        self.menuOPC_UA_Client.addAction(self.actionSubscribeEvent)
        self.menuOPC_UA_Client.addAction(self.actionUnsubscribeEvents)
        self.menuOPC_UA_Client.addAction(self.actionFocusTree)
        self.menuSettings.addAction(self.actionDark_Mode)
        self.menuSettings.addAction(self.actionClient_Application_Certificate)
        self.menuBar.addAction(self.menuOPC_UA_Client.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.addrComboBox, self.connectOptionButton)
        MainWindow.setTabOrder(self.connectOptionButton, self.connectButton)
        MainWindow.setTabOrder(self.connectButton, self.disconnectButton)
        MainWindow.setTabOrder(self.disconnectButton, self.treeView)
        MainWindow.setTabOrder(self.treeView, self.attrView)
        MainWindow.setTabOrder(self.attrView, self.attrRefreshButton)
        MainWindow.setTabOrder(self.attrRefreshButton, self.subView)
        MainWindow.setTabOrder(self.subView, self.refView)
        MainWindow.setTabOrder(self.refView, self.evView)
        MainWindow.setTabOrder(self.evView, self.spinBoxNumberOfPoints)
        MainWindow.setTabOrder(self.spinBoxNumberOfPoints, self.spinBoxIntervall)
        MainWindow.setTabOrder(self.spinBoxIntervall, self.buttonApply)
        MainWindow.setTabOrder(self.buttonApply, self.logTextEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpcUa Client"))
        self.menuOPC_UA_Client.setTitle(_translate("MainWindow", "Act&ions"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.attrDockWidget.setWindowTitle(_translate("MainWindow", "&Attributes"))
        self.attrRefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.connectOptionButton.setText(_translate("MainWindow", "Connect options"))
        self.subDockWidget.setWindowTitle(_translate("MainWindow", "S&ubscriptions"))
        self.refDockWidget.setWindowTitle(_translate("MainWindow", "&References"))
        self.evDockWidget.setWindowTitle(_translate("MainWindow", "&Events"))
        self.graphDockWidget.setWindowTitle(_translate("MainWindow", "&Graph"))
        self.labelNumberOfPoints.setText(_translate("MainWindow", "Number of Points"))
        self.labelIntervall.setText(_translate("MainWindow", "Intervall [s]"))
        self.buttonApply.setText(_translate("MainWindow", "Apply"))
        self.actionConnect.setText(_translate("MainWindow", "&Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "&Disconnect"))
        self.actionDisconnect.setToolTip(_translate("MainWindow", "Disconnect from server"))
        self.actionSubscribeDataChange.setText(_translate("MainWindow", "&Subscribe to data change"))
        self.actionSubscribeDataChange.setToolTip(
            _translate("MainWindow", "Subscribe to data change from selected node"))
        self.actionUnsubscribeDataChange.setText(_translate("MainWindow", "&Unsubscribe to DataChange"))
        self.actionUnsubscribeDataChange.setToolTip(
            _translate("MainWindow", "Unsubscribe to DataChange for current node"))
        self.actionSubscribeEvent.setText(_translate("MainWindow", "Subscribe to &events"))
        self.actionSubscribeEvent.setToolTip(_translate("MainWindow", "Subscribe to events from selected node"))
        self.actionUnsubscribeEvents.setText(_translate("MainWindow", "U&nsubscribe to Events"))
        self.actionUnsubscribeEvents.setToolTip(_translate("MainWindow", "Unsubscribe to Events from current node"))
        self.actionCopyPath.setText(_translate("MainWindow", "Copy &Path"))
        self.actionCopyPath.setToolTip(_translate("MainWindow", "Copy path to node to clipboard"))
        self.actionCopyNodeId.setText(_translate("MainWindow", "C&opy NodeId"))
        self.actionCopyNodeId.setToolTip(_translate("MainWindow", "Copy NodeId to clipboard"))
        self.actionAddToGraph.setText(_translate("MainWindow", "Add to &Graph"))
        self.actionAddToGraph.setToolTip(_translate("MainWindow", "Add this node to the graph"))
        self.actionAddToGraph.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionRemoveFromGraph.setText(_translate("MainWindow", "Remove from Graph"))
        self.actionRemoveFromGraph.setToolTip(_translate("MainWindow", "Remove this node from the graph"))
        self.actionRemoveFromGraph.setShortcut(_translate("MainWindow", "Ctrl+Shift+G"))
        self.actionCall.setText(_translate("MainWindow", "Call"))
        self.actionCall.setToolTip(_translate("MainWindow", "Call Ua Method"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionDark_Mode.setStatusTip(_translate("MainWindow", "Enables Dark Mode Theme"))
        self.actionClient_Application_Certificate.setText(_translate("MainWindow", "Client Application Certificate"))
        self.actionFocusTree.setText(_translate("MainWindow", "FocusTree"))
        self.actionFocusTree.setShortcut(_translate("MainWindow", "Alt+T"))
