from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def emptypage(request):
    
    return HttpResponse(" Write /home in the path to go to home page ^_^ ")
    
def home(request):

    return HttpResponse("Hello World, This is my new HOME !")

