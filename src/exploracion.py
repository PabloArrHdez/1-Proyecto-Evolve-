import pandas as pd
import numpy as np
from datetime import datetime

analisis_estad =pd.read_csv("Datos/df_completo.csv")

def descripcion(analisis_estad):
    analisis_estad["fecha"] = pd.to_datetime(analisis_estad["fecha"], errors="coerce")
    analisis_estad.info()
    analisis_estad.describe()
    print(f"Este DataFrame tiene: {analisis_estad.shape[0]} filas y {analisis_estad.shape[1]} columnas")
    print(f"Este DataFrame tiene un total de: {analisis_estad.isna().sum()} valores nulos")


