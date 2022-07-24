from django.shortcuts import render

# Create your views here.

## My code ##
from django.http import HttpResponse
def greetings(request):
  message = "Hello World, This is my new HOME !"
  return HttpResponse(message)