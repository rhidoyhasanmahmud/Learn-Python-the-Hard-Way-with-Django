# Django Model

A Django model is the built-in feature that Django uses to create tables, their fields, and various constraints.

In short, Django Models is the SQL of Database one uses with Django.

SQL (Structured Query Language) is complex and involves a lot of different queries for creating, deleting, updating or any other stuff related to database.

Django models simplify the tasks and organize tables into models. Generally, each model maps to a single database table.

Django models provide simplicity, consistency, version control and advanced metadata handling. Basics of a model include –

1. Each model is a Python class that subclasses django.db.models.Model.
2. Each attribute of the model represents a database field.
3. With all of this, Django gives you an automatically-generated database-access API.

```py

from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

```

Django maps the fields defined in Django models into table fields of the database as shown below.

![Django-Model](https://media.geeksforgeeks.org/wp-content/uploads/20191220123439/django-models.png)

## Creating a Model

```py
from django.db import models

class ModelName(models.Model):
        field_name = models.Field(**options)

```

To create a model, in geeks/models.py Enter the code,

```py
# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")

        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title
```

Whenever we create a Model, Delete a Model, or update anything in any of models.py of our project. We need to run two commands makemigrations and migrate.

makemigrations basically generates the SQL commands for preinstalled apps (which can be viewed in installed apps in settings.py)

> Python manage.py makemigrations

SQL Query to create above Model as a Table is created and

> Python manage.py migrate

creates the table in the database.

# Meta Class in Model

Model Meta is basically the inner class of your model class. Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model.

```text
class student(models.Model):
    class Meta:
        options........
```

Model Meta has a lot of options that you can give your model in its internal class meta

1. abstract

If abstract = True, this model will be an abstract base class.

```py
class student(models.Model):
  class Meta:
      abstract = True
```

2. app_label

If a model is defined outside of applications in INSTALLED_APPS, it must declare which app it belongs to:

```py
class student(models.Model):
  class Meta:
      app_label = 'myapp' # add app name here
```

3. verbose_name

verbose_name is basically a human-readable name for your model

```py

class student(models.Model):
  class Meta:
      verbose_name = "stu" # add verbose_name  here
```

4. ordering

Ordering is basically used to change the order of your model fields.

```py
class student(models.Model):
  class Meta:
      ordering = [-1] # Add ordering like this [-1] it changes the order in descending order
```

5. proxy

If we add proxy = True a model which subclasses another model will be treated as a proxy model

```py
class Teacher(models.Model):
  pass

class Student(Teacher):
  class Meta:
      proxy = True
```

6. permissions

Extra permissions to enter into the permissions table when creating this object. Add, change, delete and view permissions are automatically created for each model.

```py
lass student(models.Model):
  class Meta:
      permissions = []
```

7. db_table

We can overwrite the table name by using db_table in meta class.

```py
class student(models.Model):
  class Meta:
      db_table = 'X' # This will change the table name to X.
```

8. get_latest_by

It returns the latest object in the table based on the given field, used for typically DateField, DateTimeField, or IntegerField.

```py
class student(models.Model):
  class Meta:
      get_latest_by = "order_date" # Return the latest by ascending order_date.


```
