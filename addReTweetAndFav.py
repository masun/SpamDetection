#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

# Input file donde está la data.
ifile1  = open("datasets/dumpCaraotaDigitalCNNELaPatilla.csv", "rb")
reader1 = csv.reader(ifile1)
ifile2  = open("datasets/datos_separados/featureVectorsEntrenamientoWithTopic.csv", "rb")
reader2 = csv.reader(ifile2)
# Output file donde se almacenará los datos de cada topico.

ofile  = open("datasets/datos_separados/featureVectorsEntrenamientoWithTopicRetuitFav.csv", "wb")
writer = csv.writer(ofile, delimiter=',')


conRetuitsFav = []
for row in reader1:
    conRetuitsFav.append(row)

conTopic = []
for row in reader2:
    conTopic.append(row)

ifile1.close()
ifile2.close()

isHeader = True
for row2 in conTopic:
	if isHeader:
		row2.insert(-1,'favorite_count')
		row2.insert(-1,'retweet_count')
		writer.writerow(row2)
		isHeader = False
	else:
		for row1 in conRetuitsFav[1:]:
			if row1[0] == row2[0]:
				row2.insert(-1,row1[-8])
				row2.insert(-1,row1[-7])
				writer.writerow(row2)
				break

# Se cierran todos los archivos.


ofile.close()
