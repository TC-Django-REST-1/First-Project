from django.shortcuts import render
from django.http import HttpRequest, HttpResponse , HttpResponse 
# Create your views here.
def hello(request : HttpRequest):
    msg='Hello World, This is my new HOME !'
    return HttpResponse(msg)