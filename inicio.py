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
import time

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

    # Metodo para abrir un directorio y procesar todos los archivos XLSX
    def openFile(self, df):

        # Constructor de la case con el datafreame de conexiones global
        class Investigador:
            def __init__(self, df):
                self.df = df

        # Constructor de las instancias de cada investigador
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

        # Dialogo seleccionar directorio
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askdirectory()
        files = os.listdir(file_path)

        # Volcado a la terminal principal de tiempo de ejecucion de la creacion de instancias
        self.Term_princ.append('Procesando archivos en directorio...\n'+str(file_path))
        self.Term_princ.append('Creando instancias de cada investigador:\n')

        # Inicio proceso creacion de instancias
        instance_timer = time.time()
        df = pd.DataFrame()
        personas = []
        holder = {"nombre": [], "instancia": []}

        # recoleccion y limpieza de nombres de investigadores
        self.Term_princ.append('Investigadores procesados:\n')

        # Para cada archivo, crea una instancia (instancename)
        for file in files:
            excel_origen = ExcelFile(file_path + '/' + file)

            # eliminacion de la extension
            instancename = file.replace('.xlsx', '')

            # creacion de una lista con los nombres de las instancias, por cada archivo procesado,
            # se crea un nombre basado en el nombre del archivo
            personas.append(instancename)

            # Volcado en terminal de los nombres de los investigadores procesados
            self.Term_princ.append(str(instancename))


            # Creacion del dataframe que contiene la informacion de cada los investigador
            cf = pd.DataFrame()
            cf = cf.append(excel_origen.parse(excel_origen.sheet_names[2]))

            # Creacion de un diccionario (holder) que contiene todas las instancias y
            # estas a su vez asociadas al nombre del investigador
            holder["nombre"].append(instancename)
            holder["instancia"].append(persona(instancename, cf))

            # Cracion del dataframe que contiene la informacion combinada
            # de todos los investigafores del directorio
            df = df.append(cf)

        # Captura y volcado en terminal del tiempo de creacion de instancias y dataframe global
        instance_times_top = time.time()
        total_instance_time = instance_times_top-instance_timer
        self.Term_princ.append('\nTiempo de recoleccion de instancias de investigadores:  '+str(total_instance_time)+'s.')

       # Funcion que compara un string dado (k) con los nombres del diccionario y
        # devuelve la instancia asociada (classperson)
        # def get_key(k):
        #     for key, value in holder.items():
        #         i =0
        #         for x in value:
        #             i = i + 1
        #             if x == k:
        #                 classperson = holder.get('instancia')[i-1]
        #                 return classperson
        #
        #     return "key doesn't exist"
        #
        # # definicion de la persona de interes para la extraccion de informacios
        # # de su instancia correspondiente
        # position = get_key('ALBIO DE JESUS GUTIERREZ AMADOR')
        # print(position.issn)



        # Inicio del proceso de construcciond e la red
        network_construction_start = time.time()

        # llamada a la case constructora investigador a partir del dataframe global df
        a = Investigador(df)

        # Inicia la funcion initialnetwork con el dataframe df y devuelve la red G
        figura = initialNetwork(a.df)
        self.Term_princ.append('\nTiempo de recoleccion de instancias de investigadores:  '+str(total_instance_time)+'s.')
        self.Term_princ.append('\nNumero de articulos procesados:  ' + str(len(df['Titulo'])))

        # Volcado del tiempo de ejecucion de la creacion de la red a la terminal principal
        network_construction_finish = time.time()
        network_construction_time = network_construction_finish-network_construction_start

        self.Term_princ.append('Tiempo de construccion de la red:  ' + str(network_construction_time)+'s.')

        # Volcado de informacion basica de la red
        self.Term_princ.append(str(len(holder['nombre'])))
        self.Term_princ.append(nx.info(figura))


        axex = [1,2,3,4,5,6,7,8,9,10]
        axey = [30,32,34,32,33,31,29,32,35,45]
        figes = self.Graph_princ.axes.plot(axex, axey)





    def processFile(self, df):
        df = a.df
        initialNetwork(a)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()