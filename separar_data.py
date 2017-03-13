#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

# Input file donde está la data.
ifile  = open("datasets/featureVectorsDumpCaraotaDigitalCNNELaPatillaENTRENAMIENTO.csv", "rb")
reader = csv.reader(ifile)

# Output file donde se almacenará los datos de cada topico.
ofile0  = open("datasets/datos_separados/featureVectors0.csv", "wb")
ofile1  = open("datasets/datos_separados/featureVectors1.csv", "wb")
ofile2  = open("datasets/datos_separados/featureVectors2.csv", "wb")
ofile3  = open("datasets/datos_separados/featureVectors3.csv", "wb")
ofile4  = open("datasets/datos_separados/featureVectors4.csv", "wb")
ofile5  = open("datasets/datos_separados/featureVectors5.csv", "wb")
ofile6  = open("datasets/datos_separados/featureVectors6.csv", "wb")
ofile7  = open("datasets/datos_separados/featureVectors7.csv", "wb")
ofile8  = open("datasets/datos_separados/featureVectors8.csv", "wb")
ofile9  = open("datasets/datos_separados/featureVectors9.csv", "wb")

writer0 = csv.writer(ofile0, delimiter=',')
writer1 = csv.writer(ofile1, delimiter=',')
writer2 = csv.writer(ofile2, delimiter=',')
writer3 = csv.writer(ofile3, delimiter=',')
writer4 = csv.writer(ofile4, delimiter=',')
writer5 = csv.writer(ofile5, delimiter=',')
writer6 = csv.writer(ofile6, delimiter=',')
writer7 = csv.writer(ofile7, delimiter=',')
writer8 = csv.writer(ofile8, delimiter=',')
writer9 = csv.writer(ofile9, delimiter=',')


# Se leen los datos de los top topics.
dict_datos_top = csv.DictReader(open("datasets/idTuitsWithTopTopicsEntrenamiento.csv", "r"))
datos_topL =list(dict_datos_top) # Se transforma en una lista con los top_topics.
 
i = 0
isHeader = True
for row in reader:
	if isHeader:
		writer0.writerow(row)
		writer1.writerow(row)
		writer2.writerow(row)
		writer3.writerow(row)
		writer4.writerow(row)
		writer5.writerow(row)
		writer6.writerow(row)
		writer7.writerow(row)
		writer8.writerow(row)
		writer9.writerow(row)
		isHeader = False
	else:
		if datos_topL[i]['top_topic_1'] == str(0): 
			writer0.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(1): 
			writer1.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(2): 
			writer2.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(3): 
			writer3.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(4): 
			writer4.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(5): 
			writer5.writerow(row)
		if datos_topL[i]['top_topic_1'] == str(6): 
			writer6.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(7): 
			writer7.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(8): 
			writer8.writerow(row)
		elif datos_topL[i]['top_topic_1'] == str(9):
			writer9.writerow(row)
		i += 1
	# Se cierran todos los archivos.

ifile.close()
ofile0.close()
ofile1.close()
ofile2.close()
ofile3.close()
ofile4.close()
ofile5.close()
ofile6.close()
ofile7.close()
ofile8.close()
ofile9.close()
