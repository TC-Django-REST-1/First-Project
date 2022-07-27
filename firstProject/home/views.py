from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def hello(req : HttpRequest):

    res = "Hello World , I love Django!"
    
    return HttpResponse(res)