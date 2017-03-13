#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import itertools
from random import shuffle



class TweetFeatureExtractor :
    
    """
    #   Ayuda a extraer los features de cada tuit
    #
    #
    """
    
    def __init__(self, tweet_id):
        self.tweet_id = tweet_id
        self.tweetFeatureCount = dict()
        self.tweetFeatureCount["hashtags"] = 0
        self.tweetFeatureCount["mentions"] = 0
        self.tweetFeatureCount["uppercase"] = 0
        self.tweetFeatureCount["nonalpha"] = 0
        self.tweetFeatureCount["urls"] = 0
        self.tweetFeatureCount["len"] = 0
        self.tweetFeatureCount["numbers"] = 0
    
    def addFeature(self, feature) :
        self.tweetFeatureCount[feature] += 1
    
    def getFeature(self, feature) :
        return self.tweetFeatureCount[feature]
    
    def lenFeature(self, tweet) :
        self.tweetFeatureCount["len"] = len(tweet)
    
    def urlFeature(self, tweet) :
        self.tweetFeatureCount["urls"] = \
            len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet))
    
    def numbersFeature(self, tweet) :
        self.tweetFeatureCount["numbers"] = \
            len(re.findall(r'\s\d*[.,]?\d*\s', tweet))
        
    
    def extractFeatures(self, tweetText) :
        self.lenFeature(tweetText)
        self.urlFeature(tweetText)
        self.numbersFeature(tweetText)
        for word in tweetText.split(" ") :
            for letter in word:
                if not letter.isalnum() :
                    self.addFeature("nonalpha")
                if letter.isupper() :
                    self.addFeature("uppercase")
            if word.startswith("@") :
                self.addFeature("mentions")
            elif word.startswith("#") :
                self.addFeature("hashtags")
                
            
            
        



class Tweet :
    
    """
    #   Guarda un tuit
    #
    #
    """
    
    
    def __init__(self, text, tweet_id) :
        self.text = text
        self.tweet_id = tweet_id
        self.label = None
    
    def classify(self) :
        self.label = raw_input("Text: "+self.text+" \n\n Input label: (y/n) (s for stopping): ")
        # Si el usuario no quiere seguir clasificando
        if self.label == 's' :
            self.label = None
            raise BreakIt
    

# Esto se usa para salir de la clasificacion sin perder el generador. Es un truco.
class BreakIt(Exception): pass

class TweetsBank :
    
    """
    #   Administra todos los tuits
    #
    #
    """
    
    def __init__(self, csvFilename) :
        self.tweets = []
        input_file = csv.DictReader(open(csvFilename, "r"))
        # row es cada linea del csv de entrada. Es un diccionario
        # cuyas keys son los nombres de cada columna del archivo
        for key,row in enumerate(input_file):
            if ("id" not in row) and ("tweet_id" not in row) :
                tweet = Tweet(row["text"], str(key))
            elif "tweet_id" in row :
                tweet = Tweet(row["text"], row["tweet_id"])
            elif "id" in row :
                tweet = Tweet(row["text"], row["id"])
            
            self.tweets.append(tweet)
        self.tweetGenerator = self.generateTweets()
    
    def generateTweets(self) :
        for tweet in self.tweets :
            yield tweet
    
    def classifyTweets(self) :
        
        for tweet in self.tweetGenerator :
            try:
                tweet.classify()
            except BreakIt:
                print("Stop")
                self.tweetGenerator = \
                    itertools.chain([tweet], self.tweetGenerator)
                break
        
    
    def saveTweets(self, filename) :
        with open(filename, "w") as newTweetsFile:
            newTweetsFile.write("tweet_id,")
            newTweetsFile.write("hashtags,")
            newTweetsFile.write("mentions,")
            newTweetsFile.write("uppercase,")
            newTweetsFile.write("nonalpha,")
            newTweetsFile.write("urls,")
            newTweetsFile.write("len,")
            newTweetsFile.write("numbers,")
            newTweetsFile.write("spam")
            newTweetsFile.write("\n")
            for tweet_raw in self.tweets :
                tweet = TweetFeatureExtractor(tweet_raw.tweet_id)
                tweet.extractFeatures(tweet_raw.text)
                newTweetsFile.write(str(tweet.tweet_id))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["hashtags"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["mentions"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["uppercase"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["nonalpha"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["urls"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["len"]))
                newTweetsFile.write(",")
                newTweetsFile.write(str(tweet.tweetFeatureCount["numbers"]))
                newTweetsFile.write(",")
                if tweet_raw.label :
                    newTweetsFile.write(tweet_raw.label)
                else :
                    newTweetsFile.write("?")
                newTweetsFile.write("\n")
            newTweetsFile.close()
    
    def updateFeatures(self, featuresCSVFilename):
        input_file = csv.DictReader(open(featuresCSVFilename, "r+"))
        label_dict = dict()
        for key,row in enumerate(input_file):
            if ("id" not in row) and ("tweet_id" not in row) :
                label_dict[str(key)] = row["spam"]
            elif "tweet_id" in row :
                label_dict[row["tweet_id"]] = row["spam"]
            elif "id" in row :
                label_dict[row["id"]] = row["spam"]
        
        for tweet in self.tweets :
            tweet.label = label_dict[tweet.tweet_id]
        
        self.saveTweets(featuresCSVFilename)


# Se abre el archivo generado por birdwatcher
with open("datasets/dumpCaraotaDigitalCNNELaPatilla.csv","r") as f :
    l = f.readlines()
    f.close()

# Se desordenan sus lineas
ran = l[1:]
shuffle(ran)
header = [l[0]]

# Se guardan las lineas desordenadas
with open("datasets/dumpCaraotaDigitalCNNELaPatillaRANDOM.csv","w") as f :
    f.writelines(header + ran)
    f.close()

# Se lee el archivo fuente y se crea un banco de tuits
twitterBankOfVen = TweetsBank("datasets/dumpCaraotaDigitalCNNELaPatillaRANDOM.csv")

# Se clasifican manualmente algunos de ellos
twitterBankOfVen.classifyTweets()

# Se calculan los features y se guarda todo junto con la clasificacion manual
# de arriba
twitterBankOfVen.saveTweets("datasets/featureVectorsDumpCaraotaDigitalCNNELaPatilla.csv")
