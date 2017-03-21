from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_tweets_for_account/$', views.get_tweets_for_account, name='get_tweets_for_account'),
]