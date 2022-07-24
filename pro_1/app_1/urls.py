from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app_1-home')
               
               ]