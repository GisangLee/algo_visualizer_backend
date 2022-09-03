from .common import *

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "172.26.151.84", "algo_backend"]

MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS

STATIC_ROOT = os.path.join(PROJ_DIR, "static")