# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import datetime, os, calendar
########## Suplementary function

# 1. month and number
def monthNum(num):
    return {1 : "Ene", 2:"Feb",3:"Mar",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10: "Oct",11:"Nov",12:"Dic"}[num]


########Import data
# Read filenames in directory
folderdir = os.getcwd()+"\\Data\\Pre-dispatch"
filetype = ".xlsx"
files = [f for f in os.listdir(folderdir) if "Despacho" in f]
# Order files by date
names = []
yrs = [20,21]
for y in yrs:
    bag = [f for f in files if str(y) in f[-14:-9]]
    for i in range(1,13):
        names.extend([f for f in bag if monthNum(i) in f])
# Read sheets
tabs = pd.ExcelFile("Data/Pre-dispatch/"+names[0]).sheet_names[-1]
dfs = pd.DataFrame()
for n in names:
    df = pd.read_excel("Data/Pre-dispatch/"+n, sheet_name = tabs, header = [2])
    dfs = dfs.append(df, ignore_index=True)

####### Time vector & time series properties to dataframe
t0 = datetime.datetime(2020,10,13)
timevec = [t0]
[timevec.append(timevec[-1]+datetime.timedelta(hours = 1)) for i in range(1,len(dfs))]
dfs.drop("HORA", axis = 1, inplace = True)
dfs["DateTime"] = timevec
dfs = dfs.set_index("DateTime")
dfs["Hora"] = dfs.index.hour
dfs["Dia - Mes"] = dfs.index.day
dfs["Dia - Semana"] = dfs.index.weekday

############ Data Visualization
for n,i in zip(dfs.columns[0:10], range(0,len(dfs.columns[0:10]))):
    plt.figure(num = i, figsize = (12,8))
    sb.scatterplot(data = dfs, x = "Hora", y = n)
    sb.boxplot(data = dfs, x = "Hora", y = n)
    sb.relplot(data = dfs, x = "Hora",  y = n, kind = "line")
    plt.show()    
    