# Django Forms

When one creates a Form class, the most important part is defining the fields of the form. Each field has custom validation logic, along with a few other hooks. This article revolves around various fields one can use in a form along with various features and techniques concerned with Django Forms.

Forms are basically used for taking input from the user in some manner and using that information for logical operations on databases. For example, Registering a user by taking input as his name, email, password, etc.

Django maps the fields defined in Django forms into HTML input fields. Django handles three distinct parts of the work involved in forms:

1. preparing and restructuring data to make it ready for rendering
2. creating HTML forms for the data
3. receiving and processing submitted forms and data from the client

![Djang-Forms](https://media.geeksforgeeks.org/wp-content/uploads/20200107124202/flowChart-1-1024x682.png)

```py
from django import forms

# creating a form
class GeeksForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
```

## Using Django Forms

Creating a form in Django is completely similar to creating a model, one needs to specify what fields would exist in the form and of what type. For example, to input, a registration form one might need First Name (CharField), Roll Number (IntegerField), and so on.

To create a form, in geeks/forms.py Enter the code,

```py
# import the standard Django Forms
# from built-in library
from django import forms

# creating a form
class InputForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())
```

## Render Django Forms

Django form fields have several built-in methods to ease the work of the developer but sometimes one needs to implement things manually for customizing User Interface(UI). A form comes with 3 in-built methods that can be used to render Django form fields.

{{ form.as_table }} will render them as table cells wrapped in <tr> tags
{{ form.as_p }} will render them wrapped in <p> tags
{{ form.as_ul }} will render them wrapped in <li> tags

To render this form into a view, move to views.py and create a home_view as below.

```py
from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)

```

In view, one needs to just create an instance of the form class created above in forms.py. Now let’s edit templates > home.html

```html
<form action="" method="post">
  {% csrf_token %} {{form }} <input type="submit" value=Submit">
</form>
```

Now, visit http://localhost:8000/

Link: https://www.geeksforgeeks.org/django-forms/

