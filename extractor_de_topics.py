#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Extraído de: https://de.dariah.eu/tatom/topic_model_python.html

import numpy as np
import sklearn.feature_extraction.text as text
from palabras_comunes import palabras_comunes



vectorizer = text.CountVectorizer(input='datasets/tuits_solo_texto.csv', 
                                    stop_words=palabras_comunes, 
                                    max_df=0.5)

file = open('datasets/tuits_solo_texto.csv',"r")
lineas = file.readlines()


dtm = vectorizer.fit_transform(lineas).toarray()

vocab = np.array(vectorizer.get_feature_names())

from sklearn import decomposition

num_topics = 10
num_top_words = 10
clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)


topic_words = []

for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i].encode('utf-8') for i in word_idx])

doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)

#print doctopic
print dtm.shape
for t in range(len(topic_words)):
    print("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))


