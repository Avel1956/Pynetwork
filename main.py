import networkx as nx
import matplotlib.pyplot as plt
import itertools
import numpy as np
import pandas as pd
import os



dirName = 'redes'


    # Crea carpeta si no existe
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Carpeta ", dirName, " creada")
else:
    print("Carpeta ", dirName, " ya existe")

G = nx.read_graphml('InvTest.graphml')
nx.draw(G)
print(G.order())
plt.show()