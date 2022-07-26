from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def hello(request: HttpRequest):
    text : str = 'Hello world, I love djanog !'
    return HttpResponse(text)