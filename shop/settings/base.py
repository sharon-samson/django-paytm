"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wnthprh@_#k=+z0*3$7#)*p(fenltojqu6xcxtqv$c(up-^jc9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #apps
    'textiles',
    'paytm',

    #thirdparty
    'widget_tweaks',
    # 'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
]

SITE_ID = 2

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #socialauth
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                #socialauth
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)



# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

LOGOUT_REDIRECT_URL = '/login/'



LOGIN_EXEMPT_URLS = (
    r'^logout/$',
    r'^signup/$',
    r'^admin/$',
)

LOGIN_REDIRECT_URL = 'textiles:home'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
# 'django.core.mail.backends.smtp.EmailBackend'                 
# 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = '/login/'

LOGOUT_URL = 'accounts:logout'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djangocbv@gmail.com'
EMAIL_HOST_PASSWORD = 'asiftech1234@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEBUG = True


SOCIAL_AUTH_FACEBOOK_KEY = '1137640766400537'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '40d0ef84bfe0121088497738db3cae83'  # App Secret

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}

PAYTM_MERCHANT_KEY = "Vu23quBJkVY5RXJJ"
PAYTM_MERCHANT_ID = "FVSxKW32751095468634"
HOST_URL = "http://localhost:8000"
PAYTM_CALLBACK_URL = "/paytm/response/"

if DEBUG:
    PAYTM_MERCHANT_KEY = "Vu23quBJkVY5RXJJ"
    PAYTM_MERCHANT_ID = "FVSxKW32751095468634"
    PAYTM_WEBSITE = 'WEBSTAGING'
    HOST_URL = 'http://localhost:8000'
    '''
    In sandbox enviornment you can use following wallet credentials to login and make payment.
    Mobile Number : 7777777777
    Password : Paytm12345
    This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
    '''
# PAYTM_MERCHANT_KEY = "FVSxKW32751095468634"
# PAYTM_MERCHANT_ID = "Vu23quBJkVY5RXJJ"
# HOST_URL = "http://localhost:8001"
# PAYTM_CALLBACK_URL = "/paytm/response/"

# if DEBUG:
#     PAYTM_MERCHANT_KEY = "FVSxKW32751095468634"
#     PAYTM_MERCHANT_ID = "Vu23quBJkVY5RXJJ"
#     PAYTM_WEBSITE = 'WEB_STAGING'
#     HOST_URL = 'http://localhost:8001'
#     '''
#     In sandbox enviornment you can use following wallet credentials to login and make payment.
#     Mobile Number : 7777777777
#     Password : Paytm12345
#     This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
#     '''

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())