Introduction 


This is a simple application to Create, Retrieve, Update and Delete records from a database named 'xyzcompany', and a table named 'employee' in default SQlite database Server using Django with Django user signup, login, and authentication.

Software used in this project:
Windows operating system
Python software version above 3.6,latest version can also be used.
SQlite Database can be used.
Django Web Framework software version 3.0.

Check for Python Installation
 At the command prompt type 

$ python --version

 
Creating Virtual Environment in Windows

$ python -m venv venv
 

 
Activating Virtual Environment venv
 
$ venv\scripts\activate 
 

Installing Django Web Framework 
 
$ pip install django

Check installed Django version

$ python -m django --version

Created a Django project named ‘XYZcompany’

$ django-admin startproject xyzcompany

 
Installing PyAutoGUI

$ pip install PyAutoGUI

Installing Pillow

$ pip install Pillow

Migrations
 To create databases, run the following commands on the command prompt, as shown below.
 
$ python manage.py makemigrations
$ python manage.py migrate



Start the development server to verify the project work by executing  
at the command prompt.

$ python manage.py runserver


Created SuperUser(Admin) for the website
 
$ python manage.py createsuperuser 
 
Enter your desired username and press enter.
 
Creating the app named ‘accounts’ 
  
$ python manage.py startapp accounts 
 
 



