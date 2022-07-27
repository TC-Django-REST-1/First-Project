from django.shortcuts import render
from django.http import HttpRequest,HttpResponse



def hello(request : HttpRequest):
  
    return HttpResponse(" Hello World, This is my new HOME !")

# Create your views here.
