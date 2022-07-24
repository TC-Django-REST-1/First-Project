from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def Home(request : HttpRequest):
    phrase1 : str = "Hello World my first HOME"
    return HttpResponse(phrase1)

