"""
Django settings for paradise project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r-#_do2@z0@pb*cg4)(1iegj#o1k#^k^(e1%12qema6$!1j*2p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '10.1.2.131']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'paradise_app.apps.ParadiseConfig',
    'django_extensions',
    'rest_framework',
    'bootstrap4',
    'django_google_maps',
    'django_openid_auth',
    'googleauth',

]

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_CONFIRM_EMAIL = False
COMMENTS_XTD_MAX_THREAD_LEVEL = 5  # default is 0
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'mobi.MobileDetectionMiddleware',
]

ROOT_URLCONF = 'paradise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
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

WSGI_APPLICATION = 'paradise.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'paradise_app_prueba',
        'USER': 'paradise',
        'PASSWORD': 'paradise',
        'HOST': 'localhost',
        'PORT': '5432', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL= '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_SSO_SERVER_URL = 'https://login.launchpad.net/'

AUTHENTICATION_BACKENDS = (
            'django_openid_auth.auth.OpenIDBackend',
            'django.contrib.auth.backends.ModelBackend',
            'googleauth.backends.GoogleAuthBackend',
)

# client ID from the Google Developer Console
GOOGLEAUTH_CLIENT_ID = '1026685614512-b6tf2t8q40a4fhafb8cr7d3asqv72uu0.apps.googleusercontent.com'

# client secret from the Google Developer Console
GOOGLEAUTH_CLIENT_SECRET = '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'

# your app's domain, used to construct callback URLs
GOOGLEAUTH_CALLBACK_DOMAIN = ''

# callback URL uses HTTPS (your side, not Google), default True
GOOGLEAUTH_USE_HTTPS = False

# restrict to the given Google Apps domain, default None
GOOGLEAUTH_APPS_DOMAIN = ''

# get user's name, default True (extra HTTP request)
GOOGLEAUTH_GET_PROFILE = True

# sets value of user.is_staff for new users, default False
GOOGLEAUTH_IS_STAFF = False

# list of default group names to assign to new users
GOOGLEAUTH_GROUPS = []