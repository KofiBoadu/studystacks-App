from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logout_view(request):
	"""LOG THE USER OUT"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
	"""REGISTER NEW USER"""
	if request.method != 'POST':
		#Display blank registration form
		form=UserCreationForm()

	else:
		#GET REGISTERATION DETAILS AND PROCESS
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user= form.save()
			#LOG THE USER IN AND THEN REDIRECT TO HOMEPAGE 
			authenticate_user=authenticate(username=new_user.username,password=request.POST['password1'])
			login(request, authenticate_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context= {'form':form}
	return render(request,'users/register.html',context)




