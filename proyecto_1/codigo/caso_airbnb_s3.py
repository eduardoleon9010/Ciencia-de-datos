#!/usr/bin/env python
# coding: utf-8

# # Aplicación del coeficiente de correlación de Pearson y Spearman caso de uso airbnb

# Autor: Eduardo Leon
# #### Objetivo:
# Caracterizar las distintas opciones de alojamiento que pone a disposición Airbnb en función de los precios, disponibilidad, calificaciones, características de los alojamientos, etc.
# #### Contexto:
# Airbnb, ha publicado un gran volumen de datos que permiten realizar análisis en dos sentidos, por una parte, desde el punto de vista de Airbnb, es posible identificar las preferencias y la experiencia que han tenido los distintos clientes en los diferentes puntos de alojamiento. Por otra parte, desde el punto de vista de los clientes, es posible identificar cuáles son los mejores puntos de alojamiento teniendo en cuenta el precio, las calificaciones que han recibido y los distintos comentarios. 
# #### Hipótesis:
# 
# 1. Existe algún grado de correlación lineal entre los puntajes de revisión y comunicación en los registros de Airbnb.
# 2. Existe alguna correlación entre el precio del alquiler y el número de habitaciones en las propiedades listadas en Airbnb.
# 

# In[107]:


# Importar las librerías necesarias según el análisis que se vaya a realizar
import os  # Librería para comando de sistema
import pandas as pd  # Librería para manejo de datos
import matplotlib.pyplot as plt  # Librería para gráficos
import numpy as np  # Librería para computación numérica



# In[108]:


# Especifica la ruta al archivo Excel
ruta_archivo_excel = r'D:\My Backups\Formacion\Big Data\Andes\1. Introducción a la ciencia de datos aplicada\listings_m.xlsx'

# Intenta leer el archivo Excel en un DataFrame de Pandas
try:
    # Lee el archivo Excel
    df_excel = pd.read_excel(ruta_archivo_excel)
    
    # Muestra las primeras filas del DataFrame para verificar que se haya cargado correctamente
    print(df_excel.head())
    
except Exception as e:
    print("Se produjo un error al leer el archivo Excel:", e)




# In[109]:


# Especifica la ruta al archivo Excel
ruta_archivo_excel = r'D:\My Backups\Formacion\Big Data\Andes\1. Introducción a la ciencia de datos aplicada\listings_m.xlsx'

# Intenta leer el archivo Excel en un DataFrame de Pandas
try:
    # Lee el archivo Excel
    df_excel = pd.read_excel(ruta_archivo_excel)
    
    # Filtra las columnas del DataFrame que contienen las variables específicas
    columnas_filtradas = df_excel.filter(regex='review_scores_communication|review_scores_rating|room_type')
    
    # Muestra las primeras filas del DataFrame filtrado
    print(columnas_filtradas.head())
    
except Exception as e:
    print("Se produjo un error al leer el archivo Excel:", e)



# In[110]:


# Intenta leer el archivo Excel en un DataFrame de Pandas
try:
    # Lee el archivo Excel
    df_excel = pd.read_excel(ruta_archivo_excel)
    
    # Filtra las columnas del DataFrame que contienen las variables específicas
    columnas_filtradas = df_excel[['review_scores_communication', 'review_scores_rating', 'room_type']]
    
    # Excluye los valores nulos e iguales a 0 de las dos primeras variables
    columnas_filtradas = columnas_filtradas.dropna(subset=['review_scores_communication', 'review_scores_rating'])
    columnas_filtradas = columnas_filtradas[(columnas_filtradas['review_scores_communication'] != 0) & (columnas_filtradas['review_scores_rating'] != 0)]
    
    # Muestra las primeras filas del DataFrame filtrado
    print(columnas_filtradas.head())
    
except Exception as e:
    print("Se produjo un error al leer el archivo Excel:", e)


# In[111]:


# Importar la librería necesaria
import seaborn as sns

# Definir los datos
x = columnas_filtradas['review_scores_communication']
y = columnas_filtradas['review_scores_rating']
room_type = df_excel.loc[columnas_filtradas.index, 'room_type']  # Seleccionar room_type para las filas seleccionadas

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x, y=y, hue=room_type, alpha=0.5)  # Usar seaborn para el gráfico de dispersión con colores por room_type
plt.title('Diagrama de dispersión de review_scores_communication vs review_scores_rating')
plt.xlabel('Review Scores Communication')
plt.ylabel('Review Scores Rating')
plt.legend(title='Room Type')  # Agregar leyenda
plt.grid(True)
plt.show()


# In[112]:


# Importar la librería necesaria
import seaborn as sns

# Definir los datos
x = columnas_filtradas['review_scores_rating']
y = columnas_filtradas['review_scores_communication']
room_type = df_excel.loc[columnas_filtradas.index, 'room_type']  # Seleccionar room_type para las filas seleccionadas

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=x, y=y, hue=room_type, style=room_type, markers=['o', 's', '^', 'd'], alpha=0.5)  # Usar seaborn para el gráfico de dispersión con colores y estilos de punto por room_type
plt.title('Diagrama de dispersión de review_scores_rating vs review_scores_communication')
plt.xlabel('Review Scores Rating')
plt.ylabel('Review Scores Communication')
plt.legend(title='Room Type')  # Agregar leyenda
plt.grid(True)
plt.show()






# In[113]:


from scipy.stats import spearmanr

# Filtra las columnas del DataFrame que contienen las variables cuantitativas
columnas_filtradas = df_excel[['review_scores_communication', 'review_scores_rating']]

# Excluye los valores nulos e iguales a 0 de las dos primeras variables
columnas_filtradas = columnas_filtradas.dropna(subset=['review_scores_communication', 'review_scores_rating'])
columnas_filtradas = columnas_filtradas[(columnas_filtradas['review_scores_communication'] != 0) & (columnas_filtradas['review_scores_rating'] != 0)]

# Calcula el coeficiente de correlación de Spearman
coef_spearman, p_value = spearmanr(columnas_filtradas['review_scores_communication'], columnas_filtradas['review_scores_rating'])

print("Coeficiente de correlación de Spearman:", coef_spearman)
print("Valor p:", p_value)


# ### Analis hipotesis 
# 1. Existe algún grado de correlación lineal entre los puntajes de revisión y comunicación en los registros de Airbnb.
# 
# Dado el resultado del coeficiente de correlación de Spearman de aproximadamente 0.43 y un valor p muy bajo (cercano a 0), podemos inferir que existe una correlación positiva significativa entre los puntajes de revisión y los puntajes de comunicación en los listados de Airbnb. Esto sugiere que, en general, los listados que reciben puntajes altos en comunicación también tienden a recibir puntajes altos en general.
# Sin embargo, es importante recordar que el coeficiente de correlación de Spearman evalúa la relación monótona entre las variables, no necesariamente la correlación lineal directa. Por lo tanto, aunque podemos inferir una asociación positiva entre los puntajes de revisión y comunicación, no podemos concluir directamente que haya una relación lineal entre ellas.
# 

# In[114]:


# Filtra las columnas del DataFrame que contienen las variables específicas
columnas_filtradas = df_excel.filter(regex='price|bedrooms')

# Muestra las primeras filas del DataFrame filtrado
print(columnas_filtradas.head())



# In[115]:


# Verificamos si la columna 'price' existe en el DataFrame
if 'price' in df_excel.columns:
    # Convertimos la columna 'price' a tipo numérico
    df_excel['price'] = pd.to_numeric(df_excel['price'], errors='coerce')
    # Imprimimos las primeras filas del DataFrame para verificar la conversión
    print(df_excel.head())
else:
    print("La columna 'price' no existe en el DataFrame.")


# In[116]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Especifica la ruta al archivo Excel
ruta_archivo_excel = r'D:\My Backups\Formacion\Big Data\Andes\1. Introducción a la ciencia de datos aplicada\listings_m.xlsx'

# Intenta leer el archivo Excel en un DataFrame de Pandas
try:
    # Lee el archivo Excel
    df_excel = pd.read_excel(ruta_archivo_excel)
    
    # Excluye los valores nulos, iguales a 0 y mayores a 400 en la columna 'price'
    df_excel = df_excel[(df_excel['price'].notnull()) & (df_excel['price'] != 0) & (df_excel['price'] <= 400)]
    
    # Excluye los valores mayores a 5 en la columna 'bedrooms'
    df_excel = df_excel[df_excel['bedrooms'] <= 5]
    
    # Crea diagrama de caja para 'price'
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df_excel['price'])
    plt.title('Diagrama de caja para la columna "price"')
    plt.xlabel('Precio')
    plt.show()
    
    # Crea diagrama de caja para 'bedrooms'
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df_excel['bedrooms'])
    plt.title('Diagrama de caja para la columna "bedrooms"')
    plt.xlabel('Número de habitaciones')
    plt.show()
    
except Exception as e:
    print("Se produjo un error al leer el archivo Excel:", e)


# In[117]:


# Extrae las variables de interés para el diagrama de dispersión
x = df_excel['price']
y = df_excel['bedrooms']

# Crea el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5)
plt.title('Diagrama de dispersión de price vs bedrooms')
plt.xlabel('Price')
plt.ylabel('Bedrooms')
plt.grid(True)
plt.show()


# In[118]:


# Calcula el coeficiente de correlación de Spearman
correlation_coefficient, p_value = spearmanr(df_excel['price'], df_excel['bedrooms'])

print("Coeficiente de correlación de Spearman:", correlation_coefficient)
print("Valor p:", p_value)


# ### Analisis hipotesis 
# 2. Existe alguna correlación entre el precio del alquiler y el número de habitaciones en las propiedades listadas en Airbnb
# 

# Sí, hay una correlación significativa entre el precio del alquiler y el número de habitaciones. El coeficiente de correlación de Spearman de 0.4748 indica una correlación positiva moderada entre estas dos variables. Esto sugiere que, en general, a medida que el número de habitaciones aumenta, el precio del alquiler tiende a aumentar también. Sin embargo, es importante tener en cuenta que la relación no es perfecta, ya que el coeficiente de correlación no es cercano a 1.

# ### Conclusiones
# Con base en los análisis realizados, se pueden hacer varias conclusiones:
# 
#     Existe una correlación positiva moderada entre los puntajes de revisión de comunicación y los puntajes de revisión en general. Esto sugiere que los huéspedes que dan calificaciones más altas en términos de comunicación tienden a dar calificaciones más altas en general.
# 
#     Hay una correlación positiva moderada entre el precio del alquiler y el número de habitaciones. Esto implica que, en general, a medida que el número de habitaciones aumenta, el precio del alquiler también tiende a aumentar.
# 
#     Se han excluido valores nulos, iguales a 0 y aquellos que superan ciertos umbrales (400 para el precio del alquiler y 5 para el número de habitaciones) mediante el uso de diagramas de caja (boxplot).
# 
# Los análisis sugieren que tanto la comunicación como el precio del alquiler pueden influir en las calificaciones de los huéspedes, y que el precio del alquiler está correlacionado con el número de habitaciones en las propiedades listadas. Sin embargo, es importante recordar que la correlación no implica causalidad y que otros factores también pueden influir en estas relaciones.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




