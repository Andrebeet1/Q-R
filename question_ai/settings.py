from pathlib import Path
import os
import dj_database_url
from decouple import config

# Récupérer le chemin de base
BASE_DIR = Path(__file__).resolve().parent.parent

# Charger SECRET_KEY depuis les variables d'environnement
SECRET_KEY = config('SECRET_KEY', default='django-insecure-defaultkey')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['question-ai-r7ys.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'question_ai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'question_ai.wsgi.application'

# Configuration de la base de données
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='postgresql://user:password@localhost/dbname'),
        conn_max_age=600,
        ssl_require=True
    )
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

