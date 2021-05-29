A personalized starting point using the following tools:

[Django](https://www.djangoproject.com/)

[GraphQL](https://graphql.org/)

[Graphene](https://graphene-python.org/)

[Poetry](https://python-poetry.org/)

## Setup
Start the virtual environment:
```
poetry shell
```
Install dependencies:
```
poetry install
```
Run migrations to set up your database schema:
```
python manage.py migrate
```
Load the sample data from the fixture:
```
python manage.py loaddata fixture.json
```
Create a super user for yourself:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver 8000
```
## Usage
When the development server is running, you can navigate to `localhost:8000/admin` to log into the admin portal, and navigate to `localhost:8000/graphql` to test out GraphQL queries.

Other django manage.py commands can be found [HERE](https://docs.djangoproject.com/en/3.2/ref/django-admin/)