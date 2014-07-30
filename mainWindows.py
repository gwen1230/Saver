# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created: Sat Jul 26 11:58:06 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 95)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 21, 436, 26))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Path = QtGui.QLineEdit(self.widget)
        self.Path.setObjectName(_fromUtf8("Path"))
        self.horizontalLayout.addWidget(self.Path)
        self.Add = QtGui.QPushButton(self.widget)
        self.Add.setObjectName(_fromUtf8("Add"))
        self.horizontalLayout.addWidget(self.Add)
        self.Remove = QtGui.QPushButton(self.widget)
        self.Remove.setObjectName(_fromUtf8("Remove"))
        self.horizontalLayout.addWidget(self.Remove)
        self.Print = QtGui.QPushButton(self.widget)
        self.Print.setObjectName(_fromUtf8("Print"))
        self.horizontalLayout.addWidget(self.Print)
        self.Save = QtGui.QPushButton(self.widget)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.horizontalLayout.addWidget(self.Save)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Add.setText(_translate("MainWindow", "Add", None))
        self.Remove.setText(_translate("MainWindow", "Remove", None))
        self.Print.setText(_translate("MainWindow", "Print", None))
        self.Save.setText(_translate("MainWindow", "Save", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

