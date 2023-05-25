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


    #PAGE FOR ADDING A  NEW TOPIC 
     path('new_topic/', views.new_topic, name='new_topic'),


     #PAGE FOR ADDING NEW ENTRY 

    
     path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

     #PAGE TO EDIT ENTRY 

    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),





]
