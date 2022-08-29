from .common import *

DEBUG = True

ALLOWED_HOSTS = []

THIRD_PARTY_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

STATICFILES_DIR = [
    os.path.join(PROJ_DIR, "static")
]
