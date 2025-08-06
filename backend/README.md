# This is an ecommarce project with django rest framwork

## Instractions

### Packages
django
pytest
djangorestframework


#### Install virtual Environment
`python -m venv env`
###### Activate
`env\Scripts\activate`
###### Deactivate
`deactivate`

### Install Django
`pip install django`
`django-admin startproject django_api`

pip freeze > requirments.txt

python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

pip install djangorestframework

