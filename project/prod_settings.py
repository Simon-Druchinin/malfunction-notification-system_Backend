from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'H0K0V@2iP4CXKlyyF$ENQv8z62Q3XN*B@&6!AJ^NWIF2zlRC&9KrhW3n@#2#@olbKNEdVi7'

DEBUG = False

ALLOWED_HOSTS = ["http://127.0.0.1", "http://79.141.74.221", "0.0.0.0"]

CORS_ALLOWED_ORIGINS = ["http://127.0.0.1", "http://79.141.74.221", "0.0.0.0"]

STATIC_ROOT = BASE_DIR.joinpath('static')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
