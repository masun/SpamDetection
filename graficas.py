#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

# Se leen los datos de feature, cada instancia es un diccionario
dict_datos = csv.DictReader(open("datasets/featureVectors.csv", "r"))

# Se leen los datos de los top topics.
dict_datos_top = csv.DictReader(open("datasets/idTuitsWithTopTopics.csv", "r"))

# Se leen los wordsbag.
dict_datos_wordbags = csv.DictReader(open("datasets/topicsWithTopWords.csv", "r"))

# Nombre de los atributos
nombres_atributos = ['tweet_id','hashtags','mentions','uppercase','nonalpha','urls','len','numbers']

# Wordsbag
wordsbag = []
for instancia in dict_datos_wordbags: #Para cada instancia.
	wordsbag.append((instancia[' wordsbag']).replace('\'',''))

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
vector_clasificacion = [[[0 for j in range(0,3)] for i in range(0, len(wordsbag)) ] for d in range(0, len(top_topicsL))]

datos_topL =list(dict_datos_top) # Lista con los top_topics.

# Calculo de frecuencia de los topicas para cada top topic.
i = 0 # Identificar de la fuente a usar.
for instancia in dict_datos_top: #Para cada instancia.
	for atributo in top_topicsL: # Para cada atributo de la instancia actual
		vector_topTopics[i][int(instancia[atributo])] += 1
		i += 1
	i = 0

# Calculo de frecuencias para cada clasificacion de cada topic en cada uno de los top topic.
for instancia in dict_datos: #Para cada instancia.
	j = 0
	for top_topic in top_topicsL:
		#print "Tweet " + str(i) + " en el top topic " + str(j) + " es spam?: " + instancia['spam']
		if (instancia['spam'] == 'y'):
			vector_clasificacion[j][int(datos_topL[i][top_topic])][0] += 1
		elif (instancia['spam'] == 'n'):
			vector_clasificacion[j][int(datos_topL[i][top_topic])][1] += 1
		else:
			vector_clasificacion[j][int(datos_topL[i][top_topic])][2] += 1
		j += 1
	i += 1


# Colores para cada barra.
colorsFr = ["#EC644B", "#D2527F", "#663399", "#446CB3", "#2C3E50", "#36D7B7", 
		  "#E9D460", "#F2784B", "#D35400", "#6C7A89"]


# Se dibuja el barchart para cada fuente con su top topic.
x = np.arange(len(wordsbag))     # Wordsbags de los top topics.
"""
# Hago el diagrama de cajas para cada top topic.
for i in range(0, len(top_topicsL)):
	barchart = plt.bar(x, vector_topTopics[i], align='center', color=colorsFr)
	plt.xticks(x, x)                  # Para que se pueda ver cada elemento del xaxis.
	plt.xlim(-0.5, len(wordsbag)-0.5) # Limite x de la grafica.
	plt.xlabel('Id del topic')
	plt.ylabel('Frecuencias')
	plt.title('Frecuencias de tweets asociado a un topico para el Top topic ' + str(i + 1))
	plt.show()						  # Se plotea.
"""

colorsCls = ["g","r", "b"] 
# Hago el diagrama de cajas para cada clasificacion de cada topic en cada top topic.
for i in range(0, len(vector_clasificacion)):
	for j in range(0, len(x)):
		x_pos = np.arange(len(vector_clasificacion[i][j]))
		barchart = plt.bar(x_pos, vector_clasificacion[i][j], align='center', color=colorsCls)
		plt.xticks(x_pos, ['Spam','No Spam', 'No clasificado']) # Para que se pueda ver cada elemento del xaxis.
		plt.xlim(-0.5, len(x_pos)-0.5) # Limite x de la grafica.
		plt.xlabel('Clasificacion')
		plt.ylabel('Frecuencias')
		plt.title('Frecuencias de tweets asociado al topico ' + str(j) + ' para el Top topic ' + str(i + 1))
		plt.show()						  # Se plotea.


#.-----------------------------------------------------------------------------.
