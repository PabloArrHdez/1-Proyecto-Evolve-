import pandas as pd
from datetime import datetime
import geopandas as gpd
import folium
from folium.plugins import HeatMap
from shapely.geometry import Point

df_sucio = pd.read_csv("Datos/bici_publicas_oficial_sucio.csv")
df_aire_sucio = pd.read_csv("Datos/dim_aire_sucio.csv")
df_poblacion_sucio = pd.read_csv("Datos/dim_poblacion_sucio.csv")

def filas_delete (df_sucio):
    lista_columnas = df_sucio.columns.tolist()
    df_sucio1 = df_sucio[~df_sucio.apply(lambda row: row.tolist() == lista_columnas, axis=1)]
    df_sucio1 = df_sucio[df_sucio["empty_slots"] >= 0.0]
    return df_sucio1

def columnas_transform (df_sucio1):
    nuevos_nombres = {
    "name": "empresa",
    "id": "id_empresa",
    "city": "ciudad",
    "country": "pais",
    "free_bikes": "bicis_libres",
    "empty_slots": "anclajes_vacios",
    "extraction_date": "fecha"
    }
    df_limpio = df_sucio1.rename(columns=nuevos_nombres, inplace=True)
    df_limpio = df_sucio1["fecha"] = pd.to_datetime(df_sucio1["fecha"], errors="coerce")
    df_limpio = df_sucio1["anclajes_vacios"] = pd.to_numeric(df_sucio1["anclajes_vacios"], errors="coerce").fillna(0).astype(int)
    df_limpio = df_sucio1["capacidad_estacion"] = (df_sucio1["anclajes_vacios"] + (df_sucio1["bicis_libres"]))
    df_limpio = df_sucio1["tasa_uso"] = (df_sucio1["anclajes_vacios"] / (df_sucio1["capacidad_estacion"]))
    df_limpio= df_sucio1.dropna(subset=["tasa_uso"])
    df_limpio.to_csv("Datos/bicis_publicas_limpio.csv", index=False)
    return df_limpio


def transformacion_gdtf(df_limpio):
    df_gdtf = df_limpio["geometry"] = df_limpio.apply(lambda row: Point(row["longitude"], row["latitude"]), axis=1)
    df_gdtf = gpd.GeoDataFrame(df_limpio, geometry="geometry")
    df_gdtf.to_csv("Datos/bicis_publicas_limpio_geodf.csv", index=False)
    return df_gdtf


def transformacion_aire(df_aire_sucio):
    ciudades_a_eliminar = ["Amsterdam", "Stockholm", "Zurich", "Munich"]
    df_aire_limpio = df_aire_sucio[~df_aire_sucio['Ciudad'].isin(ciudades_a_eliminar)]
    return df_aire_limpio

def tranformacion_poblacion(df_poblacion_sucio):
    ciudades_a_eliminar = ["Amsterdam", "Stockholm", "Zurich", "Munich"]
    df_poblacion_limpio = df_poblacion_sucio[~df_poblacion_sucio['Ciudad'].isin(ciudades_a_eliminar)]
    return df_poblacion_limpio