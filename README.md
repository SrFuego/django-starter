# {{ project_name }}

## Dependencies:

#### Python Version: 3.7.0

#### Common.in:

1. psycopg2

- Install `postgresql` on your system

#### Develop.in:

1. pygraphviz

- Install `graphviz` on your system
- In case you don't have graphviz, remove graphviz and pygraphviz from `requirements/develop-in`

## Run project

- `virtualenv venv -p /path/to/python` # Create virtualenv
- `. venv/Scripts/activate` # Activate virtualenv
- `pip install pip-tools` # Install pip-tools
- `pip-compile -r requirements/develop.in -o requirements-DATE.develop` #
- `pip-sync requirements-DATE.develop` #
- Open `.env` and edit
- `python manage.py runserver`

## Run coverage and generate html coverage code report

- `coverage run --source='.' manage.py test && coverage html`
- Open `htmlcov/index.html` in your browser
