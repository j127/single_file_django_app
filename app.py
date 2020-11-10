import os
import sys

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

# This loads environment variables from a .env file.
# See the .env-example file for instructions on how to create one.
from dotenv import load_dotenv
load_dotenv()

DEBUG = bool(os.environ.get("DEBUG", False))

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    print("please add a secret key to your .env file")
    sys.exit()

ALLOWED_HOSTS = []

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ),
)


def index(request):
    """This is a Django view that takes a request and sends a response.

    A Django "view" is equivalent to a "controller" in some other popular
    frameworks.
    """
    return HttpResponse("hello world")


# This is the router
urlpatterns = (
    url(r"^$", index),
)

application = get_wsgi_application()
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
