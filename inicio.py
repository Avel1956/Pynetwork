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
import weakref

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

        class persona:
            personainstancia = []
            def __init__(self, nombre, cf):
                self.__class__.personainstancia.append(weakref.proxy(self))
                self.nombre = nombre
                self.cf = cf
                self.titulo = cf['Titulo']
                self.autores = cf['Autores']
                self.year = cf['Año']
                self.revista = cf['Revista']
                self.pais = cf['País']
                self.issn = cf['ISSN']
                self.doi = cf['DOI']
                self.categoria = cf['Categoría']

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askdirectory()
        files = os.listdir(file_path)

        df = pd.DataFrame()
        personas = []
        holder = {"nombre": [], "instancia": []}
        # recoleccion y limpieza de nombres de investigadores
        for file in files:
            excel_origen = ExcelFile(file_path + '/' + file)
            instancename = file.replace('.xlsx', '')
            personas.append(instancename)

            cf = pd.DataFrame()
            cf = cf.append(excel_origen.parse(excel_origen.sheet_names[2]))

            holder["nombre"].append(instancename)
            holder["instancia"].append(persona(instancename, cf))
            df = df.append(cf)

        def get_key(k):
            for key, value in holder.items():
                i =0
                for x in value:
                    i = i + 1
                    if x == k:
                        classperson = holder.get('instancia')[i-1]
                        return classperson

            return "key doesn't exist"


        position = get_key('ALBIO DE JESUS GUTIERREZ AMADOR')
        print(position.issn)
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