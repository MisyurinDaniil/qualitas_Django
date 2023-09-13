"""
Django settings for qualitas project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if 'IS_DJANGO_DEBUG_FALSE' in os.environ:
    DEBUG = False
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    ALLOWED_HOSTS = [os.environ['SITENAME']]
else:
    DEBUG = True
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = 'django-insecure-ku-y3%=b8gz%x&4se2=4e0j*c!52#1bu=v7sreg*82xa#!r(#d'
    ALLOWED_HOSTS = ['*']

# print(type(os.environ))    
# print (DEBUG, SECRET_KEY, ALLOWED_HOSTS)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-ku-y3%=b8gz%x&4se2=4e0j*c!52#1bu=v7sreg*82xa#!r(#d'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = False

#ALLOWED_HOSTS = ['10.0.0.2', '10.0.0.4', '127.0.0.1', '109.195.227.218', '192.168.0.135']


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
    'appGetStaticPages.apps.AppgetstaticpagesConfig',
    'appProductItem.apps.AppproductitemConfig',
    'appOrders.apps.AppordersConfig',
    'ckeditor',
    'ckeditor_uploader',
    'snowpenguin.django.recaptcha3',
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

ROOT_URLCONF = 'qualitas.urls'

# DIRS
# По умолчанию: [] (Пустой список)
# Каталоги, в которых движок должен искать исходные файлы шаблонов, в порядке поиска.

# APP_DIRS
# По умолчанию: False
# Должен ли движок искать исходные файлы шаблонов внутри установленных приложений.
# По умолчанию файл settings.py, созданный django-admin startproject, устанавливает 'APP_DIRS': True.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'qualitas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
STATIC_URL = '/static/'

# Список директорий из которых нужно собирать (manage.py collectstatic) или искать в режиме dev нашу статику
# По умолчанию только директория static внутри созданных приложений (app)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "qualitas/static/")]

# Директория сбора статических файлов в одном месте для production 
# после запуска команды collectstatic - django соберет их в эту папку
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# аналогично STATIC_URL, это URL-адрес, по которому пользователи могут получить доступ к медиафайлам.
MEDIA_URL = '/media/'
# Директория для сбора статических файлов в одном месте для production
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = False

# Настройка статики из папки static в корне проекта (проект про кино)
# и файлов media
# информация из https://www.youtube.com/watch?v=WTXPLwrK398&list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq&index=8&ab_channel=DjangoSchool
# STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

###### CKEditro config ######

# Путь для загрузки файлов через CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"

# Настройка внешнего вида в админ панеле (добавляетяс функционал) CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'Youtube',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube'
        ]),
    }
}

RECAPTCHA_PUBLIC_KEY = "6LeWMsslAAAAANEINXlvxxyG7buNt6uXaZJTGLgH"
RECAPTCHA_PRIVATE_KEY = "6LeWMsslAAAAAAj9KcwJjfBtrTUVywjSInXeJV_E"
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5