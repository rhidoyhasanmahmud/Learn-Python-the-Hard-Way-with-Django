# DNS

> Inroduction of DNS

ICANN (Internet Corporation for Assigned Names and Numbers) is the global non-profit organization responsible for coordinating the Internet's core systems of unique identifiers, most notably the Domain Name System (DNS).

Domain Name System (DNS) is a protocol that is used to resolve domain names to Internet Protocol (IP) addresses. When you enter a domain name into a web browser, your computer sends a request to a DNS server to resolve the domain name to an IP address. The DNS server responds with the IP address of the website, and your computer then establishes a connection to the server at that IP address to retrieve the webpage.

DNS is an essential part of how the internet functions, as it allows humans to use easily memorable domain names rather than having to remember the numerical IP addresses of websites. It acts as a kind of directory for the internet, making it possible to locate and connect to websites and other online resources using easy-to-remember names.

> Why need DNS

DNS is needed because it allows humans to use easy-to-remember domain names to access websites and other online resources rather than having to remember the numerical IP addresses of those resources. IP addresses are difficult for humans to remember because they are long strings of numbers that are separated by periods. For example, the IP address for Google is "172.217.6.110". It is much easier to remember "google.com" than this string of numbers.

Without DNS, users would have to remember the numerical IP addresses of every website they wanted to visit, which would be extremely inconvenient and would make the internet much less user-friendly. DNS makes it possible for users to simply type a domain name into their web browser, and the DNS system will automatically resolve the domain name to the correct IP address, allowing the user to connect to the desired website or online resource.

# Web Server vs Web Hosting

A web server is a piece of computer hardware or software that is designed to host websites and provide them with access to the internet. A web server receives requests from clients (typically web browsers) and sends back responses in the form of web pages or other types of content.

Web hosting, on the other hand, refers to the service of hosting websites on a web server. A web hosting company provides the infrastructure and support necessary for a website to be accessible on the internet. This can include providing the web server, managing the domain name, and handling maintenance and security tasks.

In other words, a web server is the physical or virtual machine that serves the content of a website, while web hosting is the service that provides the web server and other resources necessary for a website to be accessed on the internet.

# MVT Architecture

Model-View-Template (MVT) is a software design pattern that separates the representation of data from the user's interaction with it. It consists of three parts:

1. Model: This is the data model that represents the underlying business logic and data. It includes the data structures, algorithms, and logic for manipulating the data.

2. View: This is the user interface (UI) that presents the data to the user and allows them to interact with it. The view layer is responsible for rendering the data in a way that is easily understandable and usable by the user.

3. Template: This is the layout or structure of the UI that defines how the data is presented to the user. The template specifies the overall design and layout of the UI, including the positioning and styling of the various elements.

In an MVT architecture, the model communicates with the view and template through a controller. The controller receives requests from the user (via the view), retrieves the appropriate data from the model, and then passes it back to the view to be displayed to the user. This separation of concerns allows for a clear separation of responsibilities and makes it easier to maintain and update the application.

# Library vs Framework

A library is a collection of pre-written code that can be used to perform common tasks. A developer can use a library by including it in their code and calling the functions or methods provided by the library. Libraries are usually designed to be flexible and can be used in a variety of contexts.

A framework, on the other hand, is a set of guidelines and tools that provide a structure for developing software applications. A framework defines the overall architecture of an application and provides a set of conventions and best practices for building and organizing the code.

The main difference between a library and a framework is that a library is a collection of functions that can be called by the developer, while a framework is a set of rules and conventions that the developer must follow in order to build the application. In this sense, a framework is more prescriptive and provides more guidance on how to structure and build the application, while a library is more flexible and can be used in a variety of contexts.

# How Django Work?

Django is a free and open-source web framework written in Python that is designed to make it easier to build and maintain web applications. It follows the Model-View-Template (MVT) architectural pattern and includes a number of features that make it well-suited for building modern, dynamic websites.

Here is a high-level overview of how a Django web application works:

A user sends a request to the web server.

1. The web server passes the request to the Django application.

2. The Django application determines which view function should handle the request based on the URL of the request.

3. The view function retrieves any necessary data from the database or other sources using the model layer of the MVT pattern.

4. The view function passes the data to a template, which is a file that contains the HTML code for the webpage as well as placeholders for the dynamic data.

5. The template is rendered by the Django template engine, which substitutes the placeholder values with the actual data and generates the final HTML code for the webpage.

6. The HTML code is returned to the user's web browser, which displays the webpage to the user.

This is just a high-level overview of the process. Django includes a number of additional features and tools that can be used to build more complex and powerful web applications.

# Django Project Structure

A Django project is a collection of Django apps that work together to build a web application. The basic structure of a Django project includes the following elements:

1. **manage.py**: This is a command-line utility that allows you to interact with the Django project. It is used to run Django commands and perform various tasks such as starting the development server, running tests, and deploying the application.

2. **settings.py**: This file contains the configuration settings for the Django project. It includes settings for database connections, installed apps, middleware, and various other options.

3. **urls.py**: This file defines the URL patterns for the Django project. It maps URLs to the views that should be called when a request is received for that URL.

4. **wsgi.py**: This file is used to deploy the Django project to a web server. It defines a WSGI (Web Server Gateway Interface) application that can be used by a web server to serve the Django application.

5. **app**: A Django app is a self-contained unit of code that performs a specific task or set of tasks. A Django project can contain one or more apps, and each app can have its own models, views, templates, and other code.

This is the basic structure of a Django project. You may also see other files and directories in a Django project, depending on the specific needs of the application.

# How wsgi work?

Web Server Gateway Interface (WSGI) is a specification for a common interface between web servers and web applications. It defines a standard way for web servers to communicate with web applications, allowing them to exchange information and process requests and responses.

WSGI is designed to provide a consistent interface for web servers and web applications, regardless of the specific implementation of either. This makes it possible for web servers and web applications written in different languages and frameworks to work together seamlessly.

Here is a high-level overview of how WSGI works:

1. A user sends a request to a web server.

2. The web server receives the request and passes it to the WSGI application.

3. The WSGI application processes the request and generates a response.

4. The WSGI application returns the response to the web server.

5. The web server sends the response back to the user's web browser.

In this process, the WSGI application acts as an intermediary between the web server and the web application. It receives requests from the web server and passes them on to the web application, and it receives responses from the web application and passes them back to the web server. This allows the web application to be decoupled from the web server, making it easier to develop and deploy.
