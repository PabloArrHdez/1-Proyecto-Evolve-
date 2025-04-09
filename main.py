import requests
import pandas as pd
import numpy as np
from datetime import datetime
import os
import geopandas as gpd
import folium
from folium.plugins import HeatMap
from shapely.geometry import Point
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
import contextily as ctx

import src.extraccion as ext
import src.transformacion as trs
import src. exploracion as exp
import src.visualizacion as vsz


if __name__ == "__main__":
    cities_of_interest = [
        "Madrid", "Barcelona", "Paris", "Berlin", "Amsterdam", 
        "Bruxelles", "Lisbon", "Vienna", "Warsaw", 
        "Budapest", "Stockholm", "Helsinki", "Oslo", "London", "Prague", "Dublin", "Zurich", 
        "Munich"]
    nuevos_nombres = {
        "name": "empresa",
        "id": "id_empresa",
        "city": "ciudad",
        "country": "pais",
        "free_bikes": "bicis_libres",
        "empty_slots": "anclajes_vacios",
        "extraction_date": "fecha"
        }
    df_sucio = pd.read_csv("Datos/bici_publicas_oficial_sucio.csv")
    lista_columnas = df_sucio.columns.tolist()
    df_sucio1 = df_sucio[~df_sucio.apply(lambda row: row.tolist() == lista_columnas, axis=1)]
    df_limpio = df_sucio1.rename(columns=nuevos_nombres)
    df_aire_sucio = pd.read_csv("Datos/dim_aire_sucio.csv")
    df_poblacion_sucio = pd.read_csv("Datos/dim_poblacion_sucio.csv")
    analisis_estad =pd.read_csv("Datos/df_completo.csv")
    geodataframe = gpd.read_file("Datos/bicis_publicas_limpio_geodf_p.csv")

    ext.extraccion_API(cities_of_interest)
    trs.filas_delete(df_sucio)
    trs.columnas_transform(df_sucio1)
    trs.transformacion_gdtf(df_limpio)
    trs.transformacion_aire(df_aire_sucio)
    trs.tranformacion_poblacion(df_poblacion_sucio)
    exp.descripcion(analisis_estad)
    exp.contraste_hipotesis_madrid(analisis_estad)
    vsz.matriz_correlacion(analisis_estad)
    vsz.grafico_distribcion_londres(analisis_estad)
    vsz.grafico_distribucion_barcelona(analisis_estad)
    vsz.grafico_distribucion_oslo(analisis_estad)
    vsz.grafico_distribucion_bruselas(analisis_estad)
    vsz.grafico_modelo_regresion_madrid(analisis_estad)
    vsz.mapa_calor_paris(geodataframe)