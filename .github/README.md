# Accela REST SDK in Python [![CircleCI](https://badgen.net/circleci/github/SFDigitalServices/accela-rest-sdk-py/master)](https://circleci.com/gh/SFDigitalServices/accela-rest-sdk-py) [![Coverage Status](https://coveralls.io/repos/github/SFDigitalServices/accela-rest-sdk-py/badge.svg?branch=master)](https://coveralls.io/github/SFDigitalServices/accela-rest-sdk-py?branch=master)

Accela REST SDK in Python

## Install
> $ pipenv install "git+https://github.com/SFDigitalServices/accela-rest-sdk-py.git@master#egg=accela-rest-sdk"

## Example usage
> from accela_rest_sdk.accela import Accela

> config = {'APP_ID' : '123', 'APP_SECRET' : 'ABC', 'AGENCY' : 'AGENCY_NAME'}  
> accela = Accela(config)

> record_id = "AGENCY-ABCDEF-00000-00123"  
> record_response = accela.records.get_records(record_id)

## Tests
> pipenv run python -m pytest tests/ --cov=accela_rest_sdk --cov-report term-missing
  
## Example app
Start up example app
> pipenv run gunicorn --reload 'examples.accela_app:run()'

Run test for example app
> pipenv run python -m pytest examples/ --cov=examples/ --cov-report term-missing

## Generate Documentation
with Pdoc
> (cd docs/pdoc && pipenv run python -m pdoc --html ../../accela_rest_sdk/sdk.py)

with Sphinx
> (cd docs/sphinx && pipenv run make html)





