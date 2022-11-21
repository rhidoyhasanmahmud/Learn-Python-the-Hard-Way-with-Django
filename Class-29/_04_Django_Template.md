# Django Template

Templates are the third and most important part of Django’s MVT Structure. A template in Django is basically written in HTML, CSS, and Javascript in a .html file.

Django framework efficiently handles and generates dynamically HTML web pages that are visible to the end-user.

Django mainly functions with a backend so, in order to provide a frontend and provide a layout to our website, we use templates.

### Configuration

Django Templates can be configured in app_name/settings.py,

```py
TEMPLATES = [
	{
		# Template backend to be used, For example Jinja
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		# Directories for templates
		'DIRS': [],
		'APP_DIRS': True,

		# options to configure
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]
```

To render a template one needs a view and a URL mapped to that view. Let’s begin by creating a view in geeks/views.py

```py
# import Http Response from django
from django.shortcuts import render

# create a function
def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)

```

Now we need to map a URL to render this view,

```py

from django.urls import path

# importing views from views..py
from .views import geeks_view

urlpatterns = [
    path('', geeks_view),
]
```

Finally create a template in templates/geeks.html,

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Homepage</title>
</head>
<body>
	<h1>Welcome to Geeksforgeeks.</h1>



<p> Data is {{ data }}</p>



	<h4>List is </h4>
	<ul>
	{% for i in list %}
	<li>{{ i }}</li>
	{% endfor %}
</body>
</html>
```

## The Django template language

> Variables :

Variables output a value from the context, which is a dict-like object mapping keys to values. The context object we sent from the view can be accessed in the template using variables of Django Template.

```text
{{ variable_name }}

My first name is {{ first_name }}. My last name is {{ last_name }}.

```

> Tags

Tags provide arbitrary logic in the rendering process. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.

```text
{% tag_name %}

{% cycle 'odd' 'even' %}
```

Link : https://www.geeksforgeeks.org/django-templates/
