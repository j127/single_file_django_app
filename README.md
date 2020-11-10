# Tiny Django App

This is a one-file Django app that is based on chapter 1 of the book [_Lightweight Django_](https://www.oreilly.com/library/view/lightweight-django/9781491946275/) (with some modifications).

**Note:** this is not the normal way to build a Django site -- it's just a proof of concept from the book. To learn how to build a Django site, check out the [official tutorial](https://www.djangoproject.com/start/).

There are some dotfiles in the repo that don't relate directly to Django. The only relevant files to the app are `app.py` and `.env-example`. Look in those files to see how it works.

## Running It

First, create a virtual environment and activate it:

```text
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Notice that the terminal prompt will change. The text `(.venv)` will probably be prefixed to the normal prompt, though it depends on your computer's settings.

Install the dependencies into the virtual environment:

```text
(.venv) $ pip install -r requrements.txt
```

Copy the `.env-example` to `.env` and add a secret key. To generate a secret key, run the following command:

```
(.venv) $ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Then run the server like this:

```text
(.venv) $ python app.py runserver
```

Visit `localhost:8000` to view the site.
