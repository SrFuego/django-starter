
# {{ project_name | title }}

## Dependencies:

#### Common.in:

1. psycopg2

    - Install `postgresql` on your system

#### Develop.in:

1. pygraphviz

    - Install `graphviz` on your system
    - In case you don't have graphviz, remove graphviz and pygraphviz from `requirements/develop-in`

## Development

- `git clone REPOSITORY_LINK` # Clone the repository
- `cd {{ project_name }}`
- `virtualenv venv -p /path/to/python` # Create virtualenv
- `. venv/Scripts/activate` # Activate virtualenv
- `pip install pip-tools`
- `pip-compile -r requirements/develop.in -o requirements-DATE.develop` # Generates a requirements file with the latest version of the dependencies up to the current date
- `pip-sync requirements-DATE.develop` # Synchronize the dependencies and versions of your virtual environment with those of the generated file
- Open `.env` and populate variables
- Set `ENVIRONMENT_MODULE` in `.env` file, alternatives are: `develop`, `testing`, `staging` and `production`.
- `python manage.py runserver`

## Run tests and generate html coverage code report

- `coverage run --source='.' manage.py test && coverage html`
- Open `htmlcov/index.html` in your browser
