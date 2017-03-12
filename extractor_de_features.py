#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
import itertools

class TweetFeatureExtractor :
    
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
            len(re.findall(r'\s[0-9]+\s', tweet))
        
    
    def extractFeatures(self, tweetText) :
        self.lenFeature(tweetText)
        self.urlFeature(tweetText)
        self.numbersFeature(tweetText)
        for word in tweetText.split(" ") :
            if word.startswith("@") :
                self.addFeature("mentions")
            elif word.startswith("#") :
                self.addFeature("hashtags")
            elif not word.isalpha() :
                self.addFeature("nonalpha")
            elif word.isupper() :
                self.addFeature("uppercase")
            
            
        

class tweetsFeatureExtractor :
    
    def __init__(self) :
        self.tweetsFeatureCount = dict()
        self.tweetsFeatureCount["hashtags"] = 0
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
            featureExtractor.extractFeatures(tweet.text)
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
        
    
    """
        self.tweetFeatureCount["hastags"] = 0
        self.tweetFeatureCount["mentions"] = 0
        self.tweetFeatureCount["uppercase"] = 0
        self.tweetFeatureCount["nonalpha"] = 0
        self.tweetFeatureCount["urls"] = 0
        self.tweetFeatureCount["len"] = 0
        self.tweetFeatureCount["numbers"] = 0
    """
    
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

twitterBankOfVen = TweetsBank("datasets/CNNEE_TUITS.csv")
twitterBankOfVen.classifyTweets()
twitterBankOfVen.saveTweets("datasets/featureVectors_CNNEE.csv")