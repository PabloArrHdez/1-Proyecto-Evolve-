import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

analisis_estad =pd.read_csv("Datos/df_completo.csv")

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