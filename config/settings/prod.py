import os
from .common import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", os.environ.get("SERVER_URL"), "https://www.algovisu.com"]

MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

STATIC_ROOT = os.path.join(PROJ_DIR, "static")