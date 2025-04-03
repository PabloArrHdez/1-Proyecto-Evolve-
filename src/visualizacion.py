import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

analisis_estad =pd.read_csv("Datos/df_completo.csv")

def matriz_correlacion (analisis_estad):
    m_corr = analisis_estad.select_dtypes(include=['float64', 'int64'])
    matriz_corr = m_corr.corr(method='pearson')
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Matriz de Correlación de Variables Numéricas', fontsize=16)
    plt.savefig("Imagenes/matriz_correlacion.png")
    plt.show();