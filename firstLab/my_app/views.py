from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def hello(request:HttpRequest):

    hello = "hi from hello page"
    return HttpResponse(hello)