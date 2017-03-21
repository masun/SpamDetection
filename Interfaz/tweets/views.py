from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import tweepy
from hacerPrediccion import detectarSpam

consumer_key =	"SS8JBcQRG5C6SRcINR6fLsmRb"
consumer_secret = "zr10cRxyHVXlElJFXj5EfpYYD3J0RKtQpqPbrq8EGNdnux9V1Y"

access_token = "843171705745035264-ihqbP8vNQ0GulGxK6OFC0ExfWjxIKN0"
access_token_secret = "K5cF9Ol6chEqM7SU0W6M8aXIwWj9sHCl6g7beYnD2PBnY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def index(request):
    return render(request, 'tweets/index.html', {})

@csrf_exempt
def get_tweets_for_account(request):
	account = request.POST.get('account', None)

	try:
		stuff = api.user_timeline(screen_name = account, count = 10, include_rts = True)
	except tweepy.TweepError as e:
	    return HttpResponse(json.dumps([]))
	
	listaTuitsConDatos = []
	for tweet in stuff :
		tuitsConDatos = dict()
		tuitsConDatos["tweetText"] = tweet.text
		tuitsConDatos["tweet_id"] = tweet.id
		tuitsConDatos["favorite_count"] = tweet.retweet_count #"1" if tweet.favorited else "0"
		tuitsConDatos["retweet_count"] = tweet.retweet_count
		listaTuitsConDatos.append(tuitsConDatos)
	
	#modeloFilename = "tweets/modelos/naivebayes.model"
	modeloFilename = "tweets/modelos/usado_en_interfaz_knn.model"
	
	predicciones = detectarSpam(listaTuitsConDatos,modeloFilename)
	
	odd=True
	data=[]
	for indx,tweet in enumerate(stuff):
		if indx >= len(predicciones) :
			break
		data.append({'text':tweet.text,'probabilidad':0.0,'spam':predicciones[indx]["predicted"] == "y"})
		

	return HttpResponse(json.dumps(data))