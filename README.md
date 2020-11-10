# Tiny Django App

This is a one-file Django app that is based on chapter 1 of the book _Lightweight Django_.

## Running It

First, create a virtual environment and install the dependencies:

```text
$ python3 -m venv .venv
$ pip install -r requrements.txt
```

Copy the `.env-example` to `.env` and add a secret key. To generate a secret key, run the following command:

```
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Then run the server like this:

```text
$ python app.py runserver
```

Visit `localhost:8000` to view the site.
