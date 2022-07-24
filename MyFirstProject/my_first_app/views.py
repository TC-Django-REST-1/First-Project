from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest):
    text = 'Hello World, This is my new HOME !'
    return HttpResponse(text)

