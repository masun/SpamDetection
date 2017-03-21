from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import tweepy

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

	odd=True
	data=[]
	for tweet in stuff:
		if not(odd):
			data.append({'text':tweet.text,'probabilidad':0.0,'spam':True})
		else:
			data.append({'text':tweet.text,'probabilidad':0.0,'spam':False})
		odd=not(odd)

	return HttpResponse(json.dumps(data))