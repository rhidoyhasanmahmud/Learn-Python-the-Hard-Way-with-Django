# Django View

Django views are part of the user interface — they usually render the HTML/CSS/Javascript in your Template files into what you see in your browser when you render a web page.

![Django-View](https://media.geeksforgeeks.org/wp-content/uploads/20200124153519/django-views.jpg)

Illustration of How to create and use a Django view using an Example. Consider a project named geeksforgeeks having an app named geeks.

After you have a project ready, we can create a view in geeks/views.py,

```py
# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime

# create a function
def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)
```

Let’s step through this code one line at a time:

1. First, we import the class HttpResponse from the django.http module, along with Python’s datetime library.
2. Next, we define a function called geeks_view. This is the view function. Each view function takes an HttpRequest object as its first parameter, which is typically named request.
3. The view returns an HttpResponse object that contains the generated response. Each view function is responsible for returning an HttpResponse object.

Let’s get this view to working, in geeks/urls.py,

```py
from django.urls import path

# importing views from views..py
from .views import geeks_view

urlpatterns = [
    path('', geeks_view),
]
```

Now, visit http://127.0.0.1:8000/,

## Types of Views

Django views are divided into two major categories:-

1. Function-Based Views
2. Class-Based Views

### Function Based Views

Function based views are writer using a function in python which receives as an argument HttpRequest object and returns an HttpResponse Object. Function based views are generally divided into 4 basic strategies, i.e., CRUD (Create, Retrieve, Update, Delete). CRUD is the base of any framework one is using for development.

Function based view Example –

```py
# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):

    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
```

After creating this model, we need to run two commands in order to create Database for the same.

```text
Python manage.py makemigrations
Python manage.py migrate
```

Now let’s create some instances of this model using shell, run form bash,

> Python manage.py shell

```py
>>> from geeks.models import GeeksModel
>>> GeeksModel.objects.create(
                       title="title1",
                       description="description1").save()
>>> GeeksModel.objects.create(
                       title="title2",
                       description="description2").save()
>>> GeeksModel.objects.create(
                       title="title2",
                       description="description2").save()
```

Now if you want to see your model and its data in the admin panel, then you need to register your model.
Let’s register this model. In geeks/admin.py,

```py
from django.contrib import admin
from .models import GeeksModel
# Register your models here.
admin.site.register(GeeksModel)
```

Let’s create a view and template for the same. In geeks/views.py,

```py
from django.shortcuts import render

# relative import of forms
from .models import GeeksModel


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)

```

Create a template in templates/list_view.html,

```html
<div class="main">
  {% for data in dataset %}. {{ data.title }}<br />
  {{ data.description }}<br />
  <hr />

  {% endfor %}
</div>
```

Let’s check what is there on http://localhost:8000/

## Class Based Views

Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:

1. Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
2. Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.

Class-based views are simpler and efficient to manage than function-based views. A function-based view with tons of lines of code can be converted into class-based views with few lines only. This is where Object-Oriented Programming comes into impact.

Class based view Example –
In geeks/views.py,

```py
from django.views.generic.list import ListView
from .models import GeeksModel

class GeeksList(ListView):

    # specify the model for list view
    model = GeeksModel
```

Now create a URL path to map the view. In geeks/urls.py,

```py
from django.urls import path

# importing views from views..py
from .views import GeeksList
urlpatterns = [
    path('', GeeksList.as_view()),
]
```

Create a template in templates/geeks/geeksmodel_list.html,

```html
<ul>
  <!-- Iterate over object_list -->
  {% for object in object_list %}
  <!-- Display Objects -->
  <li>{{ object.title }}</li>
  <li>{{ object.description }}</li>

  <hr />
  <!-- If objet_list is empty  -->
  {% empty %}
  <li>No objects yet.</li>
  {% endfor %}
</ul>
```

Let’s check what is there on http://localhost:8000/
