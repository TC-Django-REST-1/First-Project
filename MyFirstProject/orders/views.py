
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def hello(request:HttpRequest):
    return HttpResponse("Hello World, This is my new HOME !"
)