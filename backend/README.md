# This is an ecommarce project with django rest framwork

## Instractions

### Packages

django
pytest
pytest-django
djangorestframework
django-mptt
python-dotenv
drf-spectacular
coverage


black ###### for formatting

#### Install virtual Environment

`python -m venv env`

###### Activate

`env\Scripts\activate`

###### Deactivate

`deactivate`

### Install Django

`pip install django`
`django-admin startproject django_api`

### Save all dependance

`pip freeze > requirments.txt`

##### Get Secret key

`python manage.py shell`
`from django.core.management.utils import get_random_secret_key`
`print(get_random_secret_key())`

`pip install djangorestframework`

###### Create a new app

`python .\manage.py startapp product_app`


##### Create Api Documents
`python manage.py spectacular --file schema.yml`


#### For testing
`coverage run -m pytest`
`coverage html`
`pip install pytest-cov`
`pytest-factoryboy`
