#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Django settings for promodominus project.
# Importamos el modulo os y guardamos una variable con una ruta dinamica para que cuando cambie ubicación del proyecto
# no sea necesario cambiar mas cosas del código
import os

RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('promodominus', 'promodominus@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'promodominus',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': '5pringao',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ES'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'subidas')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(RUTA_PROYECTO,'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd*rw60so&)c#kv$f%t_d%f9rp$kr*_a+ejh!&wb15hq)8_1ib)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'promodominus.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'promodominus.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'plantillas'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'blog',
    'captcha',
    'robots_txt',
    'django.contrib.sitemaps',
    'favicon',
    'social_auth',
    'seo',
)

#Configuración de la aplicación Seo
SEO_FOR_MODELS = [
    'blog.models.Entrada'
]


#configuraciones para el social auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login/'

TWITTER_CONSUMER_KEY         = 'wtYeMde3X97moJXTjpMqfA'
TWITTER_CONSUMER_SECRET      = 'wzIfw4Fpvafji86JNmFpFyDbp4l5bUfyiyV0cCsDla4'

GOOGLE_OAUTH2_CLIENT_ID      = '801296991657-c7q7a8cc6lvotcs1r6nvsrn39sk1mng4.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '0ynAF4KKYnnrE-HN_P6x-7QJ'

FACEBOOK_APP_ID              = '554691437901657'
FACEBOOK_API_SECRET          = '542a2f17ae3ace3f2106d449fa3b816a'


STATICSITEMAPS_ROOT_SITEMAP = 'promodominus.sitemaps.sitemaps'
# Clave publica para el captcha
RECAPTCHA_PUBLIC_KEY = '6LfoNeYSAAAAACrfVds2S-hC3CQAcVTK8wZjIxTm'

# Clave privada para el captcha

RECAPTCHA_PRIVATE_KEY = '6LfoNeYSAAAAAAb_hXQKlq2M9GBUygIWSN5etVQ_'

# Captcha acepta validación ssl

RECAPTCHA_USE_SSL = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
