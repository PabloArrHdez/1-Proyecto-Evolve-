import pandas as pd
import numpy as np
from datetime import datetime
from scipy import stats

analisis_estad =pd.read_csv("Datos/df_completo.csv")

def descripcion(analisis_estad):
    analisis_estad["fecha"] = pd.to_datetime(analisis_estad["fecha"], errors="coerce")
    analisis_estad.info()
    analisis_estad.describe()
    print(f"Este DataFrame tiene: {analisis_estad.shape[0]} filas y {analisis_estad.shape[1]} columnas")
    print(f"Este DataFrame tiene un total de: {analisis_estad.isna().sum()} valores nulos")

def contraste_hipotesis_madrid(analisis_estad):
    df_madrid = analisis_estad[analisis_estad['Ciudad'] == 'Madrid']
    df_madrid = df_madrid.dropna(subset=['bicis_libres', 'tasa_uso'])
    correlacion, p_valor = stats.pearsonr(df_madrid['bicis_libres'], df_madrid['tasa_uso'])
    print(f"Coeficiente de correlación de Pearson: {correlacion:.2f}")
    print(f"Valor p: {p_valor:.4f}")
    if p_valor < 0.05:
        print("Rechazamos la hipótesis nula: El número de bicicletas libres en Madrid influye en la tasa de uso.")
    else:
        print("No podemos rechazar la hipótesis nula: No hay evidencia suficiente para afirmar que el número de bicicletas libres en Madrid influye en la tasa de uso.")


