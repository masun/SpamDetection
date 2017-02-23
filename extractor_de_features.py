#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import itertools

class TweetFeatureExtractor :
    
    def __init__(self, tweet_id):
        self.tweet_id = tweet_id
        self.tweetFeatureCount = dict()
        self.tweetFeatureCount["hastags"] = 0
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
            len(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet))
    
    def extractFeatures(self, tweetText) :
        self.lenFeature(tweetText)
        self.urlFeature(tweetText)
        for word in tweet.split(" ") :
            if word.startswith("@") :
                self.addFeature("mentions")
            elif word.startswith("#") :
                self.addFeature("hashtags")
            elif not word.isalpha() :
                self.addFeature("nonalpha")
            elif word.isdigit() :
                self.addFeature("numbers")
            elif word.isupper() :
                self.addFeature("uppercase")
            
            
        

class tweetsFeatureExtractor :
    
    def __init__(self) :
        self.tweetsFeatureCount = dict()
        self.tweetsFeatureCount["hastags"] = 0
        self.tweetsFeatureCount["mentions"] = 0
        self.tweetsFeatureCount["uppercase"] = 0
        self.tweetsFeatureCount["nonalpha"] = 0
        self.tweetsFeatureCount["urls"] = 0
        self.tweetsFeatureCount["len"] = 0
        self.tweetsFeatureCount["numbers"] = 0
        
        self.tweetCount = 0
    
    def addFeatures(self, featureExtractor) :
        for key in self.tweetsFeatureCount :
            self.tweetsFeatureCount[key] += featureExtractor.getFeature(key)
    
    def extractFeatures(self, tweets) :
        
        for tweet in tweets :
            self.tweetCount += 1
            featureExtractor = TweetFeatureExtractor(tweet.tweet_id)
            featureExtractor.extracFeatures(tweet.text)
            self.addFeatures(featureExtractor)
        
    
    


class Tweet :
    
    def __init__(self, text, tweet_id) :
        self.text = text
        self.tweet_id = tweet_id
        self.label = None
    
    def classify(self) :
        self.label = raw_input("Text: "+self.text+" \n\n Input label: (y/n) (s for stopping): ")
        if self.label == 's' :
            self.label = None
            raise BreakIt
    

class BreakIt(Exception): pass

class TweetsBank :
    
    def __init__(self, csvFilename) :
        self.tweets = []
        input_file = csv.DictReader(open(csvFilename, "r"))
        for key,row in enumerate(input_file):
            if "id" not in row :
                tweet = Tweet(row["text"], key)
            else :
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
        

twitterBankOfVen = TweetsBank("datasets/tuits_solo_texto.csv")
twitterBankOfVen.classifyTweets()

twitterBankOfVen.classifyTweets()