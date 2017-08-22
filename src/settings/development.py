from src.settings.base import *

SECRET_KEY = 's3cr3tk3y'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = []
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
