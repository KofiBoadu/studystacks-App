from django.shortcuts import render
from .models import Topic 



# Create your views here.


#creating the homepage view 
def index(request):
	"""The homepage for learning logs"""
	return render(request,'learning_logs/index.html')

#CREATING THE TOPICS VIEW 

def topics(request):
	"""SHOW ALL TOPICS"""
	topics= Topic.objects.order_by('date_added')
	context= {'topics':topics}
	return render(request, "learning_logs/topics.html",context)

#GET A TOPIC AND ALL THE ENTRIES ON THAT TOPIC

def topic(request,topic_id):
	"""SHOW A SINGLE TOPIC AND ALL THE ENTRIES"""
	topic= Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	context= {'topic':topic,'entries':entries}
	return render(request,"learning_logs/topic.html",context)
