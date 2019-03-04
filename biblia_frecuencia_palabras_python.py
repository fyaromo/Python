# -*- coding: utf-8 -*-
''' 
Proyecto: Hallar frecuencia de palabras de un libro en formato txt
Tareas:
    1. Cargar el libro en formato txt
    2. Preprocesar el texto
    3. Hallar frecuencia de palabras
    4. Graficar en una nube de palabras las 100 con mayor frecuencia
Fecha: 03-03-2019
Autor: Fredy Yarney Romero Moreno
'''

#importar librerías
import re
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud
from collections import Counter
from PIL import Image

# cargar el libro y en minúsculas
documento = open('biblia_reina_valera_1960.txt', 'r')

# cargar las palabras vacías - stopwords en español
palabras_vacias = set(stopwords.words('spanish'))

# adicionar otras palabras vacías si es el caso
nuevas_palabras_vacias = ['cada','otra1','otra2']
palabras_vacias = set(palabras_vacias.union(nuevas_palabras_vacias))


# cargar la imágen que servirá de máscara
mascara_cruz= np.array(Image.open("cruz.png"))

# declarar el diccionario que recibirá las palabras del texto y su frecuencia
frecuencia_palabras = {}

# convertir el documento en minúsculas
texto = documento.read().lower()

# obtener del texto solamente los caracteres alfabéticos y vocales con acento 
patron_coincidencia = re.findall(r'\b[a-z,á,é,í,ó,ú,ñ]{3,20}\b', texto)

# eliminar las palabras vacías
patron_coincidencia = [word for word in patron_coincidencia if word not in palabras_vacias]

# generar el diccionario con la fercuencia de palabras
for palabra in patron_coincidencia:
    cantidad = frecuencia_palabras.get(palabra,0)
    frecuencia_palabras[palabra] = cantidad + 1

# preparar el diccionario para la nube de palabras
nube_palabras_diccionario = Counter(frecuencia_palabras)
    
# configurar y generar la nube de palabras con máscara
nube_palabras = WordCloud(width = 900, height = 900, 
                          background_color="white", 
                          max_words=500, 
                          mask=mascara_cruz,
                          contour_width=20, 
                          contour_color='steelblue').generate_from_frequencies(nube_palabras_diccionario)

# mostrar la nube de palabras
plt.figure(figsize=(15,8))
plt.imshow(nube_palabras)
plt.axis("off")

# guardar la nube de palabras en una imagen
nube_palabras.to_file("nube_biblia_cruz.png")


# configurar y generar la nube de palabras sin máscara
nube_palabras = WordCloud(width = 900, height = 900, 
                          background_color="black", 
                          max_words=500, 
                          contour_width=20, 
                          contour_color='steelblue').generate_from_frequencies(nube_palabras_diccionario)

# mostrar la nube de palabras
plt.figure(figsize=(15,8))
plt.imshow(nube_palabras)
plt.axis("off")

# guardar la nube de palabras en una imagen
nube_palabras.to_file("nube_biblia_normal.png")
