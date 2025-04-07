import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import geopandas as gpd
import folium
from folium.plugins import HeatMap
from shapely.geometry import Point

analisis_estad =pd.read_csv("Datos/df_completo.csv")
geodataframe = gpd.read_file("Datos/bicis_publicas_limpio_geodf_p.csv")

def matriz_correlacion (analisis_estad):
    m_corr = analisis_estad.select_dtypes(include=['float64', 'int64'])
    matriz_corr = m_corr.corr(method='pearson')
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Matriz de Correlación de Variables Numéricas', fontsize=16)
    plt.savefig("Imagenes/matriz_correlacion.png")
    plt.show();

def grafico_distribcion_londres(analisis_estad):
    analisis_london = analisis_estad[analisis_estad['Ciudad'] == 'London']
    media = analisis_london['bicis_libres'].mean()
    mediana = analisis_london['bicis_libres'].median()
    moda = stats.mode(analisis_london['bicis_libres'], keepdims=True)[0][0]
    desviacion_tipica = analisis_london['bicis_libres'].std()
    plt.figure(figsize=(12, 6))
    sns.histplot(analisis_london, x='bicis_libres', kde=True, bins=30, color='skyblue', label='Distribución')
    plt.axvline(media, color='red', linestyle='--', linewidth=1.5, label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-', linewidth=1.5, label=f'Mediana: {mediana:.2f}')
    plt.axvline(moda, color='purple', linestyle='-.', linewidth=1.5, label=f'Moda: {moda:.2f}')
    plt.axvline(media + desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'+1 Desv. Típica: {media + desviacion_tipica:.2f}')
    plt.axvline(media - desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'-1 Desv. Típica: {media - desviacion_tipica:.2f}')
    plt.title('Distribución disponibilidad de bicicletas en Londres', fontsize=16)
    plt.xlabel('Disponibilidad', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("Imagenes/distribucion_bicicletas_londres.png")
    plt.show();

def grafico_distribucion_barcelona(analisis_estad):
    analisis_barcelona = analisis_estad[analisis_estad['Ciudad'] == 'Barcelona']
    media = analisis_barcelona['bicis_libres'].mean()
    mediana = analisis_barcelona['bicis_libres'].median()
    moda = stats.mode(analisis_barcelona['bicis_libres'], keepdims=True)[0][0]
    desviacion_tipica = analisis_barcelona['bicis_libres'].std()
    plt.figure(figsize=(12, 6))
    sns.histplot(analisis_barcelona, x='bicis_libres', kde=True, bins=30, color='skyblue', label='Distribución')
    plt.axvline(media, color='red', linestyle='--', linewidth=1.5, label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-', linewidth=1.5, label=f'Mediana: {mediana:.2f}')
    plt.axvline(moda, color='purple', linestyle='-.', linewidth=1.5, label=f'Moda: {moda:.2f}')
    plt.axvline(media + desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'+1 Desv. Típica: {media + desviacion_tipica:.2f}')
    plt.axvline(media - desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'-1 Desv. Típica: {media - desviacion_tipica:.2f}')
    plt.title('Distribución disponibilidad de bicicletas en Barcelona', fontsize=16)
    plt.xlabel('Disponibilidad', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("Imagenes/distribucion_bicicletas_barcelona.png")
    plt.show();

def grafico_distribucion_oslo(analisis_estad):
    analisis_oslo = analisis_estad[analisis_estad['Ciudad'] == 'Oslo']
    media = analisis_oslo['bicis_libres'].mean()
    mediana = analisis_oslo['bicis_libres'].median()
    moda = stats.mode(analisis_oslo['bicis_libres'], keepdims=True)[0][0]
    desviacion_tipica = analisis_oslo['bicis_libres'].std()
    plt.figure(figsize=(12, 6))
    sns.histplot(analisis_oslo, x='bicis_libres', kde=True, bins=30, color='skyblue', label='Distribución')
    plt.axvline(media, color='red', linestyle='--', linewidth=1.5, label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-', linewidth=1.5, label=f'Mediana: {mediana:.2f}')
    plt.axvline(moda, color='purple', linestyle='-.', linewidth=1.5, label=f'Moda: {moda:.2f}')
    plt.axvline(media + desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'+1 Desv. Típica: {media + desviacion_tipica:.2f}')
    plt.axvline(media - desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'-1 Desv. Típica: {media - desviacion_tipica:.2f}')
    plt.title('Distribución disponibilidad de bicicletas en Oslo', fontsize=16)
    plt.xlabel('Disponibilidad', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("Imagenes/distribucion_bicicletas_oslo.png")
    plt.show();

def grafico_distribucion_bruselas(analisis_estad):
    analisis_bruselas = analisis_estad[analisis_estad['Ciudad'] == 'Bruxelles']
    media = analisis_bruselas['bicis_libres'].mean()
    mediana = analisis_bruselas['bicis_libres'].median()
    moda = stats.mode(analisis_bruselas['bicis_libres'], keepdims=True)[0][0]
    desviacion_tipica = analisis_bruselas['bicis_libres'].std()
    plt.figure(figsize=(12, 6))
    sns.histplot(analisis_bruselas, x='bicis_libres', kde=True, bins=30, color='skyblue', label='Distribución')
    plt.axvline(media, color='red', linestyle='--', linewidth=1.5, label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-', linewidth=1.5, label=f'Mediana: {mediana:.2f}')
    plt.axvline(moda, color='purple', linestyle='-.', linewidth=1.5, label=f'Moda: {moda:.2f}')
    plt.axvline(media + desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'+1 Desv. Típica: {media + desviacion_tipica:.2f}')
    plt.axvline(media - desviacion_tipica, color='orange', linestyle='--', linewidth=1.5, label=f'-1 Desv. Típica: {media - desviacion_tipica:.2f}')
    plt.title('Distribución disponibilidad de bicicletas en Bruselas', fontsize=16)
    plt.xlabel('Disponibilidad', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("Imagenes/distribucion_bicicletas_bruselas.png")
    plt.show();

def grafico_modelo_regresion_madrid(analisis_estad):
    df_madrid = analisis_estad[analisis_estad['Ciudad'] == 'Madrid']
    X = df_madrid['tasa_uso']
    Y = df_madrid['bicis_libres']
    X = sm.add_constant(X)
    modelo = sm.OLS(Y, X).fit()
    print(modelo.summary())
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='tasa_uso', y='bicis_libres', data=df_madrid, color='blue', alpha=0.7, label='Datos')
    plt.plot(df_madrid['tasa_uso'], modelo.predict(X), color='red', label='Regresión lineal')
    predicciones = modelo.get_prediction(X)
    pred_summary = predicciones.summary_frame(alpha=0.05)
    plt.fill_between(df_madrid['tasa_uso'], 
                    pred_summary['mean_ci_lower'], 
                    pred_summary['mean_ci_upper'], 
                    color='pink', alpha=0.3, label='Intervalo de confianza 95%')
    plt.title('Modelo de Regresión Lineal: Bicicletas Libres vs Tasa de Uso en Madrid', fontsize=16)
    plt.xlabel('Tasa de Uso', fontsize=12)
    plt.ylabel('Bicicletas Libres', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("modelo_regresion_lineal_madrid.png")
    plt.show();

def mapa_calor_paris(geodataframe):
    geodataframe = geodataframe.drop(columns=["geometry"])
    geodataframe['geometry'] = geodataframe.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)  # Crear la columna 'geometry' a partir de 'latitude' y 'longitude' #
    geodataframe = gpd.GeoDataFrame(geodataframe, geometry='geometry')  # Convertir el DataFrame en un GeoDataFrame #
    # Asignar un sistema de referencia de coordenadas (CRS)
    # Usualmente, las coordenadas de latitud y longitud están en WGS 84 (EPSG:4326)
    geodataframe.set_crs(epsg=4326, inplace=True)
    # Filtrar los datos para la ciudad de París
    paris_data = geodataframe[geodataframe['Ciudad'] == 'Paris']
    # Extraer latitud y longitud de la columna 'geometry'
    paris_data['lat'] = paris_data.geometry.y
    paris_data['lon'] = paris_data.geometry.x
    paris_data['lat'] = pd.to_numeric(paris_data['lat'], errors='coerce')
    paris_data['lon'] = pd.to_numeric(paris_data['lon'], errors='coerce')
    paris_data['tasa_uso'] = pd.to_numeric(paris_data['tasa_uso'], errors='coerce')
    paris_data = paris_data.dropna(subset=['lat', 'lon', 'tasa_uso'])
    mapa_paris = folium.Map(location=[paris_data['lat'].mean(), paris_data['lon'].mean()], zoom_start=12)
    # Preparar los datos para el mapa de calor
    heat_data = paris_data[['lat', 'lon', 'tasa_uso']].values.tolist()
    # Agregar el mapa de calor
    HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(mapa_paris)
    mapa_paris.save("mapa_calor_paris.html")
    mapa_paris;