
# Django Project Template
The purpose of this project is to use a Django project template when wanting to create a new Django project. 
Some features on this project are:
 - Development and Production settings with customizable environment variables
 - Basic and Modular URL routing to start developing ASAP
 - gitignore file
 - Basic Django/Python libraries
 - Basic CSS styling classes
 - `base.html` file that imports Bootstrap, jQuery, and FontAwesome as CDNs
 
 Note: If you're only interested in splitting the development and deployment settings, you can use the `only-settings` branch

## Requirements
- [Python 3.9](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)

## Environment File
- Take a look at the `.env.example` and make your own `.env`
- The location of this file should be on the same level as the `.env.example` file
- The `DJANGO_SETTINGS_MODULE`, `DJANGO_SECRET_KEY`, and `DATABASE_URL` are mandatory environment variables.
 
 Your `.env` for development settings should look like the following:
```
DJANGO_SETTINGS_MODULE=app.settings.development
DJANGO_SECRET_KEY=your-django-secret-key
DATABASE_URL=postgres://YourUserName:YourPassword@YourHost:5432/YourDatabase
```  
 

## Installation
Make sure to be on the same level as the `Pipfile` and `Pipfile.lock` files.

```
# Install Virtual Environment:
$ pipenv install

# Activate Virtual Environemnt:
$ pipenv shell
```  

## Usage
```bash
# Database migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Start Django Application
$ python manage.py runserver 
```