import networkx as nx
import matplotlib.pyplot as plt
import itertools as iter
import numpy as np
import pandas as pd
from pandas import *
import os
# iniciar graph


def initialNetwork (dataf):

    G = nx.Graph()



    # expandir los autores separados con comas en la hoja original
    def explode(dataf, lst_cols, fill_value='', preserve_index=False):
        # make sure `lst_cols` is list-alike
        if (lst_cols is not None
            and len(lst_cols) > 0
            and not isinstance(lst_cols, (list, tuple, np.ndarray, pd.Series))):
            lst_cols = [lst_cols]
        # all columns except `lst_cols`
        idx_cols = dataf.columns.difference(lst_cols)
        # calculate lengths of lists
        lens = dataf[lst_cols[0]].str.len()
        # preserve original index values
        idx = np.repeat(dataf.index.values, lens)
        # create "exploded" DF
        res = (pd.DataFrame({
                    col:np.repeat(dataf[col].values, lens)
                    for col in idx_cols},
                    index=idx)
                 .assign(**{col:np.concatenate(dataf.loc[lens>0, col].values)
                                for col in lst_cols}))
        # append those rows that have empty lists
        if (lens == 0).any():
            # at least one list in cells is empty
            res = (res.append(dataf.loc[lens==0, idx_cols], sort=False)
                      .fillna(fill_value))
        # revert the original index order
        res = res.sort_index()
        # reset index if requested
        if not preserve_index:
            res = res.reset_index(drop=True)
        return res

    df2 = explode(dataf.assign(Autores=dataf.Autores.str.split(',')), 'Autores')

    # reducir el dataframe a los articulos y autores
    df3 = df2 [['Titulo', 'Autores']]

    # agrupar los autores por titulo de articulo
    df4 = df3.groupby('Titulo').Autores.apply(lambda x: list(iter.combinations(x, 2)))

    # crear un vector con las combinaciones de pares de autores para cada articulo
    a = []
    for name in df4.index:
        a.append(df4.loc[name])
    b = []
    for sublist in a:
        for val in sublist:
            b.append(val)


    # añadir la informacion de las relaciones
    G.add_edges_from(b)

    # representar
    plt.subplot(121)
    nx.draw(G, with_labels=True)
    plt.show()
    print(nx.info(G))

    # from matplotlib.pyplot import figure
    # figure(figsize=(10, 8))
    # nx.draw_shell(G, with_labels=True)



