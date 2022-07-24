from email import message
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    message = """<h1>Hello World, This is my new HOME !</h1>"""
    return HttpResponse(message)
