# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erevna.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Ventana de texto, terminal principal
        self.Term_princ = QtWidgets.QTextBrowser(self.centralwidget)
        self.Term_princ.setGeometry(QtCore.QRect(10, 10, 461, 541))
        self.Term_princ.setObjectName("Term_princ")

        # ventana de la figura integrada en desarrollo
        self.Graph_princ = MplCanvas(self.centralwidget)
        self.Graph_princ.setGeometry(QtCore.QRect(480, 10, 541, 541))
        self.Graph_princ.setObjectName("Graph_princ")



        # boton de salida de la aplicacion
        self.pushExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit.setGeometry(QtCore.QRect(377, 600, 93, 28))
        self.pushExit.setObjectName("pushExit")

        # Menu de opciones
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        self.menuErevna = QtWidgets.QMenu(self.menubar)
        self.menuErevna.setObjectName("menuErevna")

        # Opcion procesar'
        self.menuProcess = QtWidgets.QMenu(self.menubar)
        self.menuProcess.setObjectName("menuProcess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Opcion cargar directorio
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)

        # Opcion guardar
        self.actionSave.setObjectName("actionSave")

        # opcion salir
        self.actionExec = QtWidgets.QAction(MainWindow)
        self.actionExec.setObjectName("actionExec")

        self.menuErevna.addSeparator()

        self.menuErevna.addSeparator()

        # Accion de cargar
        self.menuErevna.addAction(self.actionLoad)

        # accion de guardar
        self.menuErevna.addAction(self.actionSave)

        # accion salir
        self.menuProcess.addAction(self.actionExec)


        self.menubar.addAction(self.menuErevna.menuAction())

        # Accion procesar
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

