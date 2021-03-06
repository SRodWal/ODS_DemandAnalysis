# -*- coding: utf-8 -*-

import pandas as pd
import datetime, os, calendar
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
#######
def monthNum(num):
    return {1 : "Ene", 2:"Feb",3:"Mar",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10: "Oct",11:"Nov",12:"Dic"}[num]


####### Leer archivos en carpeta de datos
folderdir = os.getcwd()+"\\Data\\Pre-dispatch"
filetype = ".xlsx"
files = [f for f in os.listdir(folderdir) if "PreDespacho_Final_" in f]

######## Ordenar archivos por fecha e importar archivos
yrs = [19,20,21]
names = []
for y in yrs:
    bag = [f for f in files if str(y) in f[18:-9]]
    for m in range(1,13):
        names.extend([f for f in bag if monthNum(m) in f[18:-9]])
# Tab con costos marginales
tabs = pd.ExcelFile("Data/Pre-dispatch/"+names[0]).sheet_names[-1]

        
dfs = pd.DataFrame()
dfs_store = []
for f in names:
    df = pd.read_excel("Data/Pre-dispatch/"+f, sheet_name = tabs, header = [2])
    df = df.rename(columns = {df.columns[0]: 'Time'})
    if df.loc[0][3]=="$/MWh":
        df.drop(index = 0, axis = 0, inplace = True)       
    dfs = dfs.append(df, ignore_index = True)

for name in dfs.columns[1:len(dfs.columns)]:
    dfs[name] = dfs[name].astype(float)
#### Hora inicial de estudio Primero de junio del 19
t0 = datetime.datetime(2020, 10, 13)
timevec = [t0]
for i in range(1,len(dfs)):
    timevec.append(timevec[-1]+datetime.timedelta(hours = 1))
dfs["Time"] = timevec  
dfs = dfs.set_index("Time")    
###### Definicion de plantas
site = dfs.columns[50] # Guaymas
site = dfs.columns[64] # Guaicama
###### Series de tiempo
dfs["Año"] = dfs.index.year
dfs["Mensual"] = dfs.index.month
dfs["Mes por dia"] = dfs.index.day
dfs["Semana por dia"] = dfs.index.weekday
dfs["Por hora"] = dfs.index.hour

# Graficas
plt.figure(num = 1, figsize = (12, 6))
dfs[dfs.columns[50]].plot(marker='.', alpha=0.2, figsize=(12, 6))
plt.ylabel("Precios $/MWh")
plt.xlabel("Tiempo")
plt.title("Costos Marginales - "+site)
plt.show()

plt.figure(num = 2, figsize = (10, 6))
sb.boxplot(data = dfs, x = 'Año', y = dfs.columns[50])
plt.title("Costos Marignales Promedio Anuales")
plt.show()

datype = ["Mensual", "Mes por dia", "Semana por dia", "Por hora"]
for tp, num in zip(datype, range(1,len(datype)+1)):
    plt.figure(num = num, figsize = (10,6))
    plt.title("Comparacion de CM "+tp+": 2020 vs 2021")
    sb.lineplot(data = dfs.loc["2020-01":"2020-12"], x = tp, y = site, markers=True, dashes=False)
    sb.scatterplot(data = dfs.loc["2020-01":"2020-12"], x = tp, y = site, alpha = 0.1)
    sb.lineplot(data = dfs.loc["2021-01":"2021-12"], x = tp, y = site, markers=True, dashes=False)
    sb.scatterplot(data = dfs.loc["2021-01":"2021-12"], x = tp, y = site, alpha = 0.1)
    plt.legend(["2020","2021"])
    plt.show()

for tp, num in zip(datype, range(1,len(datype)+1)):
    plt.figure(num = num, figsize = (10,6))
    plt.title("Promedio CM Global "+tp)
    sb.lineplot(data = dfs.loc["2020-01":"2021-12"], x = tp, y = site, markers=True, dashes=False)
    sb.scatterplot(data = dfs.loc["2020-01":"2021-12"], x = tp, y = site, alpha = 0.1)
    plt.show()

plt.figure(num = 10, figsize = (10,6))
plt.title("Distribucion de precios")
sb.distplot(dfs[site].loc["2019-1":"2019-12"])
sb.distplot(dfs[site].loc["2020-1":"2020-12"])
sb.distplot(dfs[site].loc["2021-1":"2021-12"])
plt.legend(["2019","2020","2021"])
plt.show()
