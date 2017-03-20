#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

# Input file donde está la data.
ifile  = open("datasets/featureVectorsDumpCaraotaDigitalCNNELaPatillaENTRENAMIENTO.csv", "rb")
reader = csv.reader(ifile)

# Output file donde se almacenará los datos de cada topico.
ofile  = open("datasets/datos_separados/featureVectorsEntrenamientoWithTopic.csv", "wb")

writer = csv.writer(ofile, delimiter=',')

# Se leen los datos de los top topics.
dict_datos_top = csv.DictReader(open("datasets/idTuitsWithTopTopicsEntrenamiento.csv", "r"))
datos_topL =list(dict_datos_top) # Se transforma en una lista con los top_topics.

i = 0
isHeader = True
for row in reader:
	if isHeader:
		row.insert(-1,'topic_id')
		writer.writerow(row)
		isHeader = False
	else:
		if datos_topL[i]['top_topic_1'] == str(0):
			row.insert(-1,0)
		elif datos_topL[i]['top_topic_1'] == str(1):
			row.insert(-1,1)
		elif datos_topL[i]['top_topic_1'] == str(2):
			row.insert(-1,2)
		elif datos_topL[i]['top_topic_1'] == str(3):
			row.insert(-1,3)
		elif datos_topL[i]['top_topic_1'] == str(4):
			row.insert(-1,4)
		elif datos_topL[i]['top_topic_1'] == str(5):
			row.insert(-1,5)
		if datos_topL[i]['top_topic_1'] == str(6):
			row.insert(-1,6)
		elif datos_topL[i]['top_topic_1'] == str(7):
			row.insert(-1,7)
		elif datos_topL[i]['top_topic_1'] == str(8):
			row.insert(-1,8)
		elif datos_topL[i]['top_topic_1'] == str(9):
			row.insert(-1,9)
		writer.writerow(row)
		i += 1
	# Se cierran todos los archivos.

ifile.close()
ofile.close()
