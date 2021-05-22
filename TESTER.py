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