"""DEFINE URL PATTERNS FOR LEARNING LOGS"""
from django.urls import path
from . import views 


app_name = 'learning_logs'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    #SHOW ALL TOPICS PAGE PATH
    path('topics/', views.topics, name='topics'),

    #DETAIL PAGE FOR A SINGLE TOPIC 

    path('topics/<int:topic_id>/', views.topic, name='topic'),


]
