# Bicicletas públicas en ciudades europeas - Data Analysis


## Overview
Este proyecto de datos se centra en el uso de las bicicletas públicas que existen en diferentes ciudades europeas. El proyecto incluye datos relacionados con el número de bicicletas que se usan y están disponibles, el número de plazas que tiene cada estación de bicicletas, así como su localización geográfica, y el precio por utilizarlas, la población de las ciudades y el nivel de contaminación que hay durante el periodo de tiempo que dura el análisis. Su objetivo es ofrecer una comprensión de la disposición que hay en las diferentes ciudades del análisis.

## Data sources

- API Web - [CityBikes](https://api.citybik.es/v2/)
- Busqueda Web


## Workflow

1. Identificar un conjunto de datos de interés, a partir de una fuente pública.

2. Recogida de datos adicionales:


    Una vez identificado el conjunto de datos principal, el proyecto pasó a la fase de mejora mediante la recopilación de datos adicionales. Para ello, se investigó y buscó información en las diferentes páginas web para extraer información.

3. Limpieza y transformación de los datos:

    Esto incluyó la eliminación de valores atípicos, la estandarización de formatos y la resolución de cualquier incoherencia en los datos.

4. EDA: 

    Análisis Exploratorio de Datos, para comprender mejor la correlación dentro del conjunto de datos.

5. Visualización:

    Generación de gráficos y diagramas que representen eficazmente los resultados del análisis exploratorio de datos. Estas visualizaciones ayudan a comunicar los resultados con claridad.

## Hipótesis

1. ¿Cuál es el nivel de correlación en cada una de las variables?

2. ¿Cómo es la distribución de disponibilidad de bicicletas en ciudades como Londres, Barcelona, Oslo y, Bruselas? Ciudades con diferencias culturales y geográficas. 

3. Basándose en una correlación alta entre la tasa de uso y el número de bicicletas disponibles, ¿cómo es el modelo de regresión lineal de la capital de España?

4. ¿Cuáles son las estaciones con mayor tasa de uso en la ciudad de París?

## Análisis


A partir de los conjuntos de datos diferentes. Creación del conjunto de datos final sobre el que trabajar.

Composición del dataset final:

- 247.905 Filas, 12 columnas.
- Información en las columnas:
    empresa, id_empresa, ciudad, pais, bicis_libres, anclajes_vacios, latitude, longitude, fecha, capacidad_estacion, tasa_uso, geometry



## Resultados

1. Correlación de variables numéricas.

![image](Imagenes/matriz_correlacion.png)

    Indicador medianamente alto entre tasa de uso "tasa_uso" y bicicletas disponibles "bicis_libres"
    
Vamos a ver el modelo de regresión lineal de las variables anteriormente dichas en la ciudad de Madrid

![image](Imagenes/modelo_regresion_lineal_madrid.png)



2. ¿Es diferente la distribución de bicicletas públicas libres en las ciudades europeas, o se comporta igual?

![image](Imagenes/distribucion_bicicletas_londres.png) 

Aparentemente, en Londres, ciudad más habitada de Europa, el comportamiento de las bicis disponibles a lo largo de los días de análisis es exponencial. 

¿Y las demás ciudades?

Veamos: 

    - Barcelona

![image](Imagenes/distribucion_bicicletas_barcelona.png)


    - Oslo

![image](Imagenes/distribucion_bicicletas_oslo.png)


    - Bruselas

![image](Imagenes/distribucion_bicicletas_bruselas.png)

Como podemos ver en los gráficos de las ciudades señaladas, salvo Bruselas, la distribución de las bicicletas disponibles para su uso se comporta de una forma exponencial. La mayor frecuencia de disponibilidad de bicicletas es cero y a medida que van aumentando el número de bicicletas disponibles, la frecuencia disminuye, con medias en torno al 4 y casi 12 bicicletas públicas  disponibles durante la franja de tiempo de estudio. 

Pero Bruselas, a diferencia del resto de ciudades, los resultados obtenidos muestran un comportamiento un tanto de distribución normal, donde la mayor frecuencia de bicicletas disponibles está entre 9 y 10 bicicletas en todo el periodo de tiempo de estudio. Comparte también prácticamente la media con la moda, diferencia de 1 bicicleta. 


3. ¿Cuáles son las estaciones más utilizadas por los parisinos y demás habitantes?


![html](Imagenes/mapa_calor_paris.html)

Dentro del mapa generado de la ciudad metropolitana de París, se observa que la estaciones más usadas  son las más próximas a monumentos importantes y céntricos. Esto puede  deberse a que las bicis, a través de bonos diarios, pueden usarla más los turistas que los propios parisinos. Un análisis más acertado sería ver como es la demanda de bicicletas privadas en la ciudad y ver si ha aumentado o disminuido, o ver la cantidad de inscripciones al servicio de bicicletas públicas ¿Hay más número de bonos diarios que bonos mensuales? Eso nos puede dar pistas sobre como se comporta la población local de la capital de Francia. 



## Conclusiones

As we see in the data, evolution stops for no one. While there are some brands that kept track of innovation and thus uppered their rank, there are other brands for example Dior, that decided to stay with the classics, and even though their decacy it's not super noticable it still follows a descending pattern. 

An that is mostly because of the focuse each brand gives to visibility, user popularity, and introducing and adapting the brand strategies with the new technologies.

We also can prove that Runways nowadays are ysed as a lifestyle event and are not a necessity to gain visibility or popularity. As if they were, the lower ranked brands would be participating in the maximum number possible of shows. And our data shows otherwise.