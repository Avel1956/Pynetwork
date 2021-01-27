# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erevna.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Term_princ = QtWidgets.QTextBrowser(self.centralwidget)
        self.Term_princ.setGeometry(QtCore.QRect(10, 10, 461, 541))
        self.Term_princ.setObjectName("Term_princ")
        self.Graph_princ = QtWidgets.QGraphicsView(self.centralwidget)
        self.Graph_princ.setGeometry(QtCore.QRect(480, 10, 541, 541))
        self.Graph_princ.setObjectName("Graph_princ")
        self.pushExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit.setGeometry(QtCore.QRect(990, 730, 93, 28))
        self.pushExit.setObjectName("pushExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        self.menuErevna = QtWidgets.QMenu(self.menubar)
        self.menuErevna.setObjectName("menuErevna")
        self.menuProcess = QtWidgets.QMenu(self.menubar)
        self.menuProcess.setObjectName("menuProcess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExec = QtWidgets.QAction(MainWindow)
        self.actionExec.setObjectName("actionExec")
        self.menuErevna.addSeparator()
        self.menuErevna.addSeparator()
        self.menuErevna.addAction(self.actionLoad)
        self.menuErevna.addAction(self.actionSave)
        self.menuProcess.addAction(self.actionExec)
        self.menubar.addAction(self.menuErevna.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Erevna v.0.001"))
        self.pushExit.setText(_translate("MainWindow", "Exit"))
        self.menuErevna.setTitle(_translate("MainWindow", "File"))
        self.menuProcess.setTitle(_translate("MainWindow", "Process"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExec.setText(_translate("MainWindow", "Exec"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

