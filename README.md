# Django starter template for Django 2.2 LTS with Python 3.7.4

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

- For startproject `django-admin startproject --extension=py,md,example --template=https://github.com/SrFuego/django-starter/archive/PROJECT_BRANCH.zip PROJECT_NAME`
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

- Create your virtualenv
- Activate your virtualenv
- Install Django: `pip install django`
- Create project from template: `django-admin startproject --extension=py,md,example --template=https://github.com/SrFuego/django-starter/archive/PROJECT_BRANCH.zip PROJECT_NAME`
- `cd PROJECT_NAME`
- Install pip-tools: `pip install pip-tools`
- Compile develop dependencies: `pip-compile -r requirements/develop.in -o requirements-DATE.develop`
- Synchronize the packages of your virtual environment with project dependencies: `pip-sync requirements-DATE.develop`
- Create a `.env` file from `.env.example` file and populate variables in `.env`


## Run coverage and generate html coverage code report

- `coverage run --source='.' manage.py test && coverage html`
- Open `htmlcov/index.html` in your browser
