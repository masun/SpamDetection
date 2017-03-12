#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

# Se leen los datos, cada instancia es un diccionario
dict_datos = csv.DictReader(open("datasets/featureVectors.csv", "r"))

# Nombre de los atributos
nombres_atributos = ['tweet_id','hashtags','mentions','uppercase','nonalpha','urls','len','numbers']

nro_atributos = len(nombres_atributos)

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

