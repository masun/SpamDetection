#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

# Se leen los datos de feature, cada instancia es un diccionario
dict_datos = csv.DictReader(open("datasets/featureVectors.csv", "r"))

# Se leen los datos de los top topics.
dict_datos_top = csv.DictReader(open("datasets/idTuitsWithTopTopics.csv", "r"))

# Nombre de los atributos
nombres_atributos = ['tweet_id','hashtags','mentions','uppercase','nonalpha','urls','len','numbers']

# Wordsbag
wordsbag = ['video chavista periodista sentada dtb', 'venezuela vivo cnn soyfdelrincon senal', 
			'trump donald mes opinion mexico', 'muerte dolares angeles venden prostitutas',
			'ecuador vuelta cne lomasvisto resultados', 'uu ee indocumentados inmigrantes aissami',
			'sports illustrated 2017 rubia portada', 'fotos lomasvisto anos 90 accesorios', 
			'muere brutal embarazada companeras recibir', 'jong kim nam muerte corea']

# Lista con los id para los top topics de cada fuente.
top_topicsL = ['top_topic_1', 'top_topic_2', 'top_topic_3']

nro_atributos = len(nombres_atributos)
nro_wordsbag  = len(wordsbag)

"""
#.-----------------------------------------------------------------------------.
# Graficas para los atributos.

# Lista que por cada atributo almacena una lista que contiene el valor de dicho
# atributo para cada instancia
vector_atributos = []

count = 0 # Contador de iteraciones

for instancia in dict_datos: #Para cada instancia
	vector_atributos += [[]]
	for atributo in nombres_atributos: # Para cada atributo de la instancia actual
		vector_atributos[count] += [instancia[atributo]]
	count += 1


for i in range(nro_atributos):
	atributox = nombres_atributos[i] # Atributo del eje x
	for j in range(i+1,nro_atributos):
		atributoy = nombres_atributos[j] # Atributo del eje y
		#plt.figure(atributox + "-" + atributoy) # Nombre de la imagen
		plt.title(atributox + "-" + atributoy)  # Título de la imagen
		plt.xlabel(atributox)
		plt.ylabel(atributoy)
		plt.plot(vector_atributos[i],vector_atributos[j],'o')
		plt.savefig(atributox + "-" + atributoy)

#plt.show()

#.-----------------------------------------------------------------------------.
"""
# Graficas para los top_topics.

vector_topTopics = [[0 for i in range(0, len(wordsbag)) ] for d in range(0, len(top_topicsL))]

i = 0 # Identificar de la fuente a usar.
for instancia in dict_datos_top: #Para cada instancia (fuente de datos)
	for atributo in top_topicsL: # Para cada atributo de la instancia actual
		vector_topTopics[i][int(instancia[atributo])] += 1
		i += 1
	i = 0

# Colores para cada barra.
colors = ["#EC644B", "#D2527F", "#663399", "#446CB3", "#2C3E50", "#36D7B7", 
		  "#E9D460", "#F2784B", "#D35400", "#6C7A89"]

# Se dibuja el barchart para cada fuente con su top_topic.
x = np.arange(len(wordsbag))     # Wordsbags de la fuente actual.
barchart = plt.bar(x, vector_topTopics[0], align='center', color=colors)
plt.xticks(x, x)                  # Para que se pueda ver cada elemento del xaxis.
plt.xlim(-0.5, len(wordsbag)-0.5) # Limite x de la grafica.
plt.legend()
plt.show()						  # Se plotea.

#.-----------------------------------------------------------------------------.
