# First-Project-LAB

## For your First LAB , Create a new Django Project . With 1 app , which has a view handling the following path : 
- home/

## When requested (http://127.0.0.1:8000/home), it should return the phrase :
- Hello World, This is my new HOME !



### steps: 

- create new venv and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```
- install django
```bash
pip install django
```
- start new project
```bash
django-admin startproject First_Project_LAB
```
- create app command
```
python3 manage.py startapp my_first_lab_app
```

- in my_first_lab_app/views.py
```python
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request : HttpResponse):

    phrase : str = "Hello World, This is my new HOME !"

    return HttpResponse(phrase);
```


- in First_project-LAB/urls.py
```python
from django.contrib import admin
from django.urls import path
import my_first_lab_app.views.home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
]
```

- run the server 

```bash
python3 manage.py runserver
```

- hit the http://127.0.0.1:8000/home

![response](/pics/django_lab_1.png)