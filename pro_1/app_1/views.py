from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<li>Hello World, This is my new HOME !</li>")
