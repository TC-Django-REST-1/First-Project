from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    respon:str = "Hello World, This is my new HOME !"
    return HttpResponse(respon)