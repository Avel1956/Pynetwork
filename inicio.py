from erevna_ui import *
from main import *
import tkinter as tk
from tkinter import filedialog
import networkx as nx
import matplotlib.pyplot as plt
import itertools as iter
import numpy as np
import pandas as pd
from pandas import *

# Clase principal de la interfaz
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # conector boton de salida
        self.pushExit.clicked.connect(self.closeIt)
        self.actionLoad.triggered.connect(self.openFile)
        self.actionExec.triggered.connect(self.processFile)

    # definicion para el cierre de la ventana
    def closeIt(self):
        self.close()
    # def actionLoad(self):

    def openFile(self, df):
        class Investigador:
            def __init__(self, df):
                self.df = df
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        excel_origen = ExcelFile(file_path)
        df = excel_origen.parse(excel_origen.sheet_names[2])
        a = Investigador(df)
        print(file_path)
        initialNetwork(a.df)




    def processFile(self, df):
        df = a.df
        initialNetwork(a)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()