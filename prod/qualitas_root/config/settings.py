"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
# Зададим путь для deploy версии
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-ku-y3%=b8gz%x&4se2=4e0j*c!52#1bu=v7sreg*82xa#!r(#d'
SECRET_KEY = os.environ.get('secret')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
#ALLOWED_HOSTS = ['10.0.0.2', '127.0.0.1', '109.195.227.218']

# Пропишем IP для deploy версии - localhost и IP сервера
ALLOWED_HOSTS = ['127.0.0.1', '194.87.93.249']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_cleanup.apps.CleanupConfig',
    'appGetPages.apps.AppgetpagesConfig',
    'appProductItem.apps.AppproductitemConfig',
    'appOrders.apps.AppordersConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# Перевод админ панели на русский язык
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# URL для использования при обращении пользователей к статическим файлам
# {% load static %} url({% static 'img/header_shadows.png' %})
STATIC_URL = 'static/'
# Список директорий из которых нужно собирать или искать в режиме dev нашу статику
# По умолчанию только директория static внутри созданного приложения (app)
# STATICFILES_DIRS = [
#     BASE_DIR / "config/static/"
# ]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "config/static/"),
]
# Директория сбора статических файлов в одном месте для production 
# после запуска команды collectstatic - django соберет их в эту папку
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# аналогично STATIC_URL, это URL-адрес, по которому пользователи могут получить доступ к медиафайлам.
MEDIA_URL = 'media/'
# Директория для сбора статических файлов в одном месте для production
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# APPEND_SLASH = False

# Без нее не работает авторизация в админ панеле (ругается на csrf атаку) на production server
CSRF_TRUSTED_ORIGINS=['https://qualitas.store']

sAPPEND_SLASH = False

# Настройка статики из папки static в корне проекта
# информация из https://www.youtube.com/watch?v=WTXPLwrK398&list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq&index=8&ab_channel=DjangoSchool
# STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]