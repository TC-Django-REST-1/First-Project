from django.http import HttpResponse
# Create your views here.

def homeview(request):
    return HttpResponse("Hello World, This is my new HOME !")