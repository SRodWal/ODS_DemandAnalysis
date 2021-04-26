# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:05:33 2021

@author: serw1
"""

import pandas as pd
import datetime, os, calendar
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
####### Leer archivos en carpeta de datos
folderdir = os.getcwd()+"\\Data\\Pre-dispatch"
filetype = ".xlsx"
files = [f for f in os.listdir(folderdir) if "Despacho" in f]


#### Ordenamos la lista por fecha
def monthNum(num):
    return {1 : "Ene", 2:"Feb",3:"Mar",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10: "Oct",11:"Nov",12:"Dic"}[num]

filenames = []
yrs = [20,21]
for y in yrs:
    bag = [f for f in files if str(y) in f[18:-9]] #Todos los archivos de cierto año.
    for i in range(1,13):
        filenames.extend([f for f in bag if monthNum(i) in f])
#Get worksheets
tabs = pd.ExcelFile("Data/Pre-dispatch/"+filenames[0]).sheet_names
df_tab  = []
for tab in tabs:  
    dfs = pd.DataFrame()
    for file in filenames:
        df = pd.read_excel("Data/Pre-dispatch/"+file, sheet_name = tab, header = [2])
        df.drop(df.columns[0], axis=1, inplace = True)
        dfs = dfs.append(df, ignore_index = True)
    for name in dfs.columns:
        df = dfs[name]
        df = pd.to_numeric(df, errors = "coerce")
        dfs[name] = df
    df_tab.append(dfs)
 
######### Potencia total por typo de energia
remove = [tabs[-1],tabs[3]]
for r in remove:
    tabs.remove(r)
    
Coll = []
for tab in tabs:
    tot=[]
    for i in range(0,4680):
        tot.append(sum(df_tab[tab].loc[i]))
    Coll.append(tot)
 



