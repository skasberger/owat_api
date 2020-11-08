[![Build Status](https://travis-ci.org/skasberger/owat_api.svg?branch=master)](https://travis-ci.org/skasberger/owat_api) [![Coverage Status](https://coveralls.io/repos/github/skasberger/owat_api/badge.svg?branch=master)](https://coveralls.io/github/skasberger/owat_api?branch=master) [![Documentation Status](https://readthedocs.org/projects/owat_api/badge/?version=latest)](https://owat-api.readthedocs.io/en/latest/) [![GitHub](https://img.shields.io/github/license/skasberger/owat_api.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Offene Wahlen AT API

Developed by [Stefan Kasberger](http://stefankasberger.at).

**Features**

* Tests written in [pytest]() and executed with [Travis CI](). Test coverage by [coverage]() and [python-coveralls](https://github.com/z4r/python-coveralls), viewable on [coveralls.io](https://coveralls.io/github/skasberger/ow-at_api?branch=master).
* auto-generated documentation through functions and class documentation with [sphinx](http://www.sphinx-doc.org/).

**Copyright**

* Code:  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
* Documentation:  [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)

## SETUP

This instructions are to setup the development environment, which is also the default environment.

**Prerequisites**



**Initialize database**

```bash
```

**Upgrade database**

```bash
```

**Config**


### OW AT API

**Download App**

Get the app on your computer, into your webservers directory (e. g. vhost).

```bash
```

**Install requirements**

Start the virtual environment to install the needed python packages.

```bash
pip install -r requirements.txt
```

**Set environment variables**


**Run**

Run the flask app:

```bash
```

## Development

**Install**

```bash
cd /PATH/TO/VHOST
git clone https://github.com/skasberger/owat_api.git
cd owat_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements/development.txt
pre-commit install
```

### Database Migration

After changing your SQLAlchemy models, you have to update your database. To add information about your changes, exchange "COMMENT" with your commit message.

```
flask db migrate -m "COMMENT"
flask db upgrade
```

### Testing

To execute the tests, set the application mode and unset database URI.

```
```

**tox**

To execute the tests with tox (as recommended), simply type:
```
tox
```

You can find out more about the tox configuration inside `tox.ini` and in its [documentation](https://tox.readthedocs.io).

**Coverage**

To get test coverage of codebase, use coverage.

```
coverage run main.py
coverage report -m
coverage html
```

Run tests with coverage to create a html report as an output.

```
pytest --cov-report html --cov=app tests/
```
**Coveralls**

To use Coveralls on local development:
```
pytest tests/ --doctest-modules -v --cov=app
```

And to use Coveralls on Travis-CI
```
pytest tests/ --doctest-modules -v --cov coveralls --cov-report term-missing
```

### Documentation

Use Sphinx to create class and function documentation out of the doc-strings.

```
tox -e docs
```
