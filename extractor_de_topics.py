#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Extraído de: https://de.dariah.eu/tatom/topic_model_python.html

import numpy as np
import sklearn.feature_extraction.text as text
from palabras_comunes import palabras_comunes


# Token count matrix
vectorizer = text.CountVectorizer(input='datasets/tuits_solo_texto.csv', 
                                    stop_words=palabras_comunes, 
                                    max_df=0.5,
                                    lowercase=True,
                                    strip_accents="unicode",
                                    encoding="utf-8")

file = open('datasets/tuits_solo_texto.csv',"r")
lineas = file.readlines()
file.close()

# Document term matrix
dtm = vectorizer.fit_transform(lineas).toarray()

vocab = np.array(vectorizer.get_feature_names())

from sklearn import decomposition

num_topics = 10
num_top_words = 5
clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)


topic_words = []

for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i].encode('utf-8') for i in word_idx])

doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)

#print document-vs-topic-matrix dim
print("(documents, terms) = ",dtm.shape)

#Se enlaza el id de cada tuit con los ids de sus top topics
with open("datasets/idTuitsWithTopTopics.csv","w") as fileDocTopics :
    fileDocTopics.write("tweet_id,top_topic_1,top_topic_2,top_topic_3\n")
    for i in range(len(doctopic)):
        top_topics = np.argsort(doctopic[i,:])[::-1][0:3]
        top_topics_str = ' '.join(str(t) for t in top_topics)
        #print("{}: {}".format(i, top_topics_str))
        fileDocTopics.write(str(i)+","+\
                            str(top_topics[0])+","+\
                            str(top_topics[1])+","+\
                            str(top_topics[2])+"\n")
    fileDocTopics.close()

# Se enlaza el id de cada topic con sus top words
with open("datasets/topicsWithTopWords.csv","w") as fileTopics :
    fileTopics.write("id_topic, wordsbag\n")
    for t in range(len(topic_words)):
        print("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
        fileTopics.write(str(t)+",'"+(' '.join(topic_words[t][:15]))+"'\n")
    fileTopics.close()


