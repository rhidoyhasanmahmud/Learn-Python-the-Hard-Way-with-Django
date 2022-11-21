# Django Project MVT Structure

Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application.

MVT Structure has the following three parts –

Model: The model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres).

View: The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.

Template: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

![MVT](https://media.geeksforgeeks.org/wp-content/uploads/20210606092225/image.png)

## Project Structure :

A Django Project when initialized contains basic files by default such as manage.py, view.py, etc.

manage.py- This file is used to interact with your project via the command line(start the server, sync the database… etc).

> python manage.py help

folder ( employee_site ) – This folder contains all the packages of your project. Initially, it contains four files –

_init_.py – It is a python package. It is invoked when the package or a module in the package is imported. We usually use this to execute package initialization code, for example for the initialization of package-level data.

settings.py – As the name indicates it contains all the website settings. In this file, we register any applications we create, the location of our static files, database configuration details, etc.

urls.py – In this file, we store all links of the project and functions to call.

wsgi.py – This file is used in deploying the project in WSGI. It is used to help your Django application communicate with the webserver.

WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
