from django.urls import path
from django1.views import *


urlpatterns={
    path('', home,name='home') , 
    path('register/',register,name='register'),
    path('login/',login,name='login') 
}