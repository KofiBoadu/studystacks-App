from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    # LOGIN PAGE 
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    #LOGOUT PATH
    path('logout/', views.logout_view, name='logout'),

   #REGISTRATION URL 
    path('register/', views.register, name='register'),
]

