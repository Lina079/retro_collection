# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(90, 60, 181, 21))
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 221, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddItem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAddItem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAddItem.setObjectName("btnAddItem")
        self.verticalLayout.addWidget(self.btnAddItem)
        self.btnShowItems = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnShowItems.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnShowItems.setObjectName("btnShowItems")
        self.verticalLayout.addWidget(self.btnShowItems)
        self.btnDeleteItem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDeleteItem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnDeleteItem.setObjectName("btnDeleteItem")
        self.verticalLayout.addWidget(self.btnDeleteItem)
        self.btnEditItem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnEditItem.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnEditItem.setObjectName("btnEditItem")
        self.verticalLayout.addWidget(self.btnEditItem)
        self.btnAddType = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAddType.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAddType.setObjectName("btnAddType")
        self.verticalLayout.addWidget(self.btnAddType)
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#0433ff;\">RETRO COLLECTOR</span></p></body></html>"))
        self.btnAddItem.setText(_translate("MainWindow", "Add Item"))
        self.btnShowItems.setText(_translate("MainWindow", "Show Items by Type"))
        self.btnDeleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.btnEditItem.setText(_translate("MainWindow", "Edit Item"))
        self.btnAddType.setText(_translate("MainWindow", "Add New Type"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
