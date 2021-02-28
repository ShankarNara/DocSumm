from django.conf.urls import patterns, url 
from summarizer import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))