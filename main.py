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
xl = pd.ExcelFile(file)

#print(xl.sheet_names)
df1 = xl.parse('Impro')

def network (df1):
    artdic = {0: "A1", 1: "A2", 2: "B3", 3: "C4", 4: "q5",
              5: "q11", 6: "q21", 7: "q31", 8: "q41", 9: "q51",
              10: "q12", 11: "q22", 12: "q32", 13: "q42", 14: "q52",
              15: "q13", 16: "q23", 17: "q33", 18: "q43", 19: "q53",
              20: "q14", 21: "q24", 22: "q34", 23: "q44", 24: "q54",
              25: "q15", 26: "q25", 27: "q35", 28: "q45", 29: "q55",
              30: "q16", 31: "q26", 32: "q36", 33: "q46", 34: "q56",
              35: "q17", 36: "q27", 37: "q37", 38: "q47", 39: "q57",
              40: "q18", 41: "q28", 42: "q38", 43: "q48", 44: "q58"}
