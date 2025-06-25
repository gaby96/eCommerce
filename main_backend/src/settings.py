from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('MAIN_SECRET_KEY', 'django-insecure-gy@chd!-n)@wasv445exdasdw$2y^e6aq0oz9b0!^w!bfwtw')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('MAIN_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('MAIN_ALLOWED_HOSTS', '*').split()

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_results',
    'django_celery_beat',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    'djoser',
    'store',
    'users',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': f"django.db.backends.{os.getenv('MAIN_DB_CONNECTION', 'sqlite3')}",
        'NAME': os.getenv('MAIN_DB_DATABASE', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('MAIN_DB_USERNAME', ''),
        'PASSWORD': os.getenv('MAIN_DB_PASSWORD', ''),
        'HOST': os.getenv('MAIN_DB_HOST', ''),
        'PORT': os.getenv('MAIN_DB_PORT', ''),
    }
}

# Default user model
AUTH_USER_MODEL = "users.CustomUser"

# Authentication backends
AUTHENTICATION_BACKENDS = ['users.backends.AuthenticationBackend']

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "verbose",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Celery
CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = f"redis://{os.getenv('MAIN_REDIS_HOST', 'localhost')}:{os.getenv('MAIN_REDIS_PORT', '6379')}/0"

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = [
    ("gabriel", "gabriel@outlook.com"),
    ("gabrieladdo", "gabrieladdo64@gmail.com")
]

# CORS
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:8080').split()

# Django REST framework
PAGINATION_PAGE_SIZE = 20

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": PAGINATION_PAGE_SIZE,
}

DJOSER = {
    'SERIALIZERS': {
        'current_user': 'users.api.v1.serializers.CurrentUserSerializer',
    },
}

# PayPal
PAYPAL_MODE = os.getenv("PAYPAL_MODE")
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')
