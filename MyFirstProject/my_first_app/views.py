from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request : HttpRequest):
    
    phrase : str = "test page / Home"
    
    return HttpResponse(phrase)