import networkx as nx
import itertools
import numpy as np
import pandas as pd
import os

G = nx.Graph()

dirName = 'redes'


    # Crea carpeta si no existe
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Carpeta ", dirName, " creada")
else:
    print("Carpeta ", dirName, " ya existe")

dirName = 'tempDir2/temp2/temp'
file = "c.xlsx"
x1 = pd.ExcelFile(file)

#print(xl.sheet_names)
df1 = x1.parse('Impro')

Items = ["A1", "A2", "B", "C", "CLA", "CLA1", "CLB", "LA", "LA1", "LB", "SPIMO", "PI", "PMOU", "PON", "EC", "CAR", "CC",
         "SR", "SOFT", "PP", "DI", "CCM", "CCD", "CM", "CD", "CCP", "VEP", "VED", "VEM", "FEP", "FEM", "FED", "JI",
         "PN", "PIN"]
item = ['Artículo A1']
articulos_A1 = df1.loc[(df1['SUBPRODUCTO'] == "Artículo A1")]



print (articulos_A1.columns)
print (articulos_A1.count())


