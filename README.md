# Django starter template for Django 2.1 with Python 3.7.0

## Explanation of the branches:

- master: Default readme, empty branch.

#### Projects:

- base: Django normal project template.
- rest: Django rest project template.
- graphql: Django graphql project template.

#### Apps:

- base-app: Django normal project template.
- rest-app: Django rest project template.
- graphql-app: Django graphql project template.

## Branch usage:

- For startproject `django-admin startproject --extension=py,md,env --template=https://github.com/SrFuego/django-starter/archive/PROJECT_BRANCH.zip PROJECT_NAME`
- For startapp `django-admin startapp --template=https://github.com/SrFuego/django-starter/archive/APP_BRANCH.zip APP_NAME`

## Dependencies:

#### Common.in:

1. psycopg2

- Install `postgresql` on your system

#### Develop.in:

1. pygraphviz

- Install `graphviz` on your system
- In case you don't have graphviz, remove graphviz and pygraphviz from `requirements/develop.in`

## Development

- `virtualenv venv -p /path/to/python` # Create virtualenv
- `source venv/bin/activate` # Activate virtualenv
- `pip install django`
- `django-admin startproject --extension=py,md,env --template=https://github.com/SrFuego/django-starter/archive/PROJECT_BRANCH.zip PROJECT_NAME` # Create project from template
- `cd PROJECT_NAME`
- `pip install pip-tools`
- `pip-compile -r requirements/develop.in -o requirements-DATE.develop` # Generates a requirements file with the latest version of the dependencies up to the current date
- `pip-sync requirements-DATE.develop` # Synchronize the dependencies and versions of your virtual environment with those of the generated file
- Open `.env` and populate variables
- `python manage.py runserver`

## Run coverage and generate html coverage code report

- `coverage run --source='.' manage.py test && coverage html`
- Open `htmlcov/index.html` in your browser
