A personalized starting point using the following tools:

[Django](https://www.djangoproject.com/)

[GraphQL](https://graphql.org/)

[Graphene](https://graphene-python.org/)

[Poetry](https://python-poetry.org/)

## Setup
First, start the virtual environment:
```
poetry shell
```
Then, install dependencies:
```
poetry install
```
Then, run migrations to set up your database schema:
```
python manage.py migrate
```
Then, load the sample data from the fixture:
```
python manage.py loaddata fixture.json
```
Then, create a super user for yourself:
```
python manage.py createsuperuser
```
Finally, run the development server:
```
python manage.py runserver 8000
```
## Usage
When the development server is running, you can navigate to `localhost:8000/admin` to log into the admin portal, and navigate to `localhost:8000/gql` to test out GraphQL queries.

Other django manage.py commands can be found [HERE](https://docs.djangoproject.com/en/3.2/ref/django-admin/)