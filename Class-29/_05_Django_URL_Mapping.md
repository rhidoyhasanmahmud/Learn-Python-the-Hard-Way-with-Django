# Django URL patterns

In Django, views are Python functions which take a URL request as parameter and return an HTTP response or throw an exception like 404. Each view needs to be mapped to a corresponding URL pattern. This is done via a Python module called URLConf(URL configuration)

It is a good practice to have a URLConf module for every app in Django. This module needs to be included in the root URLConf module as follows:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('books.urls')),
]
```

This tells Django to search for URL patterns in the file books/urls.py.

### URL patterns

Here’s a sample code for books/urls.py:

```py
from django.urls import path
from . import views

urlpatterns = [
	path('books/<int:pk>/', views.book_detail),
	path('books/<str:genre>/', views.books_by_genre),
	path('books/', views.book_index),
]
```

For example,

1. A URL request to /books/crime/ will match with the second URL pattern. As a result, Django will call the function views.books_by_genre(request, genre = "crime").
2. Similarly a URL request /books/25/ will match the first URL pattern and Django will call the function views.book_detail(request, pk =25).

```txt
Path convertors:
The following path convertor types are available in Django

int – Matches zero or any positive integer.
str – Matches any non-empty string, excluding the path separator(‘/’).
slug – Matches any slug string, i.e. a string consisting of alphabets, digits, hyphen and under score.
path – Matches any non-empty string including the path separator(‘/’)
uuid – Matches a UUID(universal unique identifier).
```
