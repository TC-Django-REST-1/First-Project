from django.urls import path
from testapp.views import hello_world, home

urlpatterns = [path("", home), path("hello/", hello_world)]
