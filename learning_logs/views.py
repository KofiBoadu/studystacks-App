
from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Topic
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from .forms import TopicForm






#creating the homepage view 
def index(request):
	"""The homepage for learning logs"""
	return render(request,'learning_logs/index.html')

def check_topic_owner(request,topic):
	if topic.owner != request.user:
		 raise Http404

#CREATING THE TOPICS VIEW 
@login_required
def topics(request):
	"""SHOW ALL TOPICS"""
	topics= Topic.objects.filter(owner=request.user).order_by('date_added')
	context= {'topics':topics}
	return render(request, "learning_logs/topics.html",context)


#GET A TOPIC AND ALL THE ENTRIES ON THAT TOPIC
@login_required
def topic(request,topic_id):
	"""SHOW A SINGLE TOPIC AND ALL THE ENTRIES"""
	topic= Topic.objects.get(id=topic_id)
	#make sure the topic belongs to the user 
	# if topic.owner != request.user:
	# 	raise Http404
	check_topic_owner(request,topic)

	entries=topic.entry_set.order_by('-date_added')
	context= {'topic':topic,'entries':entries}
	return render(request,"learning_logs/topic.html",context)


@login_required
def new_topic(request):
	"""ADD NEW TOPIC VIEW """
	if request.method != 'POST':
		#NO DATA HAS BEEN SUBMITTED SO CREATE A BLANK FORM
		form= TopicForm()
	else:
		#DATA HAS BEEN SUBMITTED PROCESS THE DATA
		form= TopicForm(data=request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.owner=request.user 
			new_topic.save()

			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context= {'form':form}
	return render(request,'learning_logs/new_topic.html',context)




#uses the topic id to assign to a specific topic
@login_required
def new_entry(request,topic_id):
	"""ADD A NEW ENTRY FOR A PARTICULAR TOPIC"""
	topic=Topic.objects.get(id=topic_id)

	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#NO DATA HAS BEEN SUBMITTED SO CREATE A BLANK FORM
		form= EntryForm()
	else:
		#DATA HAS BEEN SUBMITTED PROCESS THE DATA
		form= EntryForm(data=request.POST)
		if form.is_valid():
			#we should save it and make sure its get to the database 
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
	context= context= {'topic':topic,'form':form, 'topic_id': topic.id}
	return render(request,'learning_logs/new_entry.html',context)





# EDITING OUT ENTRY 
@login_required
def edit_entry(request,entry_id):
	"""Edit an existing entry """
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic 

	# check_topic_owner(request,topic)

	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request, prefill form with the current entry
		form= EntryForm(instance=entry)
	else:
		#POST DATA SUBMITTED, PROCESS DATA
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	context= {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)


