"""
Django settings for ase1 project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import social_django
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sf_a09q!3-s3fnl_s)s0u6zmi5pl*y)ro%aaj+o@p7=2r!27md'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'dashboard',
    'landing_page',
    'registration',
    'student_report',
    'rest_framework'
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

ROOT_URLCONF = 'ase1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ase1.wsgi.application'

# Databasegit
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {


        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),


        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'noman31',
        # 'USER': 'root',
        # 'PASSWORD': '#####',
        # 'PORT': '3306',


    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# # https://docs.djangoproject.com/en/2.1/topics/i18n/
# AUTHENTICATION_BACKENDS = [
#     'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
#     'social_core.backends.google.GoogleOpenId',  # for Google authentication
#     'social_core.backends.google.GoogleOAuth2',  # for Google authentication
#     'django.contrib.auth.backends.ModelBackend',
# ]
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='anksharmap@gmail.com'
EMAIL_HOST_PASSWORD ='9919590707'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='852947580202-bbjk6t1f0hatp4kk7nsd1jatikb8kqk2.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'RlG5PN9nNGdLcXxonSY_N4Sj' #Paste Secret Key

LOGIN_URL = 'registration:login'
LOGIN_REDIRECT_URL = 'dashboard:dashboard'
