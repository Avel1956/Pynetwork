import networkx as nx
import matplotlib.pyplot as plt
import itertools as iter
import numpy as np
import pandas as pd
from pandas import *
import os

G = nx.Graph()
# test

excel_origen = ExcelFile('NGG.xlsx')
df = excel_origen.parse(excel_origen.sheet_names[2])

def explode(df, lst_cols, fill_value='', preserve_index=False):
    # make sure `lst_cols` is list-alike
    if (lst_cols is not None
        and len(lst_cols) > 0
        and not isinstance(lst_cols, (list, tuple, np.ndarray, pd.Series))):
        lst_cols = [lst_cols]
    # all columns except `lst_cols`
    idx_cols = df.columns.difference(lst_cols)
    # calculate lengths of lists
    lens = df[lst_cols[0]].str.len()
    # preserve original index values
    idx = np.repeat(df.index.values, lens)
    # create "exploded" DF
    res = (pd.DataFrame({
                col:np.repeat(df[col].values, lens)
                for col in idx_cols},
                index=idx)
             .assign(**{col:np.concatenate(df.loc[lens>0, col].values)
                            for col in lst_cols}))
    # append those rows that have empty lists
    if (lens == 0).any():
        # at least one list in cells is empty
        res = (res.append(df.loc[lens==0, idx_cols], sort=False)
                  .fillna(fill_value))
    # revert the original index order
    res = res.sort_index()
    # reset index if requested
    if not preserve_index:
        res = res.reset_index(drop=True)
    return res

df2 = explode(df.assign(Autores=df.Autores.str.split(',')), 'Autores')

df3 = df2 [['Titulo', 'Autores']]

print(df3)

G.add_nodes_from(df3['Autores'] )
df4 = df3.groupby('Titulo').Autores.apply(lambda x: list(iter.combinations(x, 2)))
a = []
for name in df4.index:
    print (name)
    a.append(df4.loc[name])
b = []
for sublist in a:
    for val in sublist:
        b.append(val)

print(b)
G.add_edges_from(b)
plt.subplot(121)
nx.draw(G, with_labels=True)
plt.show()
# from matplotlib.pyplot import figure
# figure(figsize=(10, 8))
# nx.draw_shell(G, with_labels=True)



