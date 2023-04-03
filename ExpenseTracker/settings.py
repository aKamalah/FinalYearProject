import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9nc1(5yh2dltt3f&m95j(53e+$q##&dtg+3%2!$@umx%feq=wz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["akamalah.pythonanywhere.com", "127.0.0.1"]

# Application definition

# CREATE APP: python manage.py startapp 'application_name'. (Type In Terminal).
# ANY DEPENDENCIES MADE: python manage.py makemigrations, python manage.py migrate. (Type In Terminal).
# SQLITE3 DATABASE: Will Be Shown In Directory Once Initial Migration Has Been Made.

# INSTALLED_APPS: Configure Applications So That We Can Look For Models And Other Utilities Within.
INSTALLED_APPS = [
    'django.contrib.admin', # ADMIN: Django Provided Admin Interface.
    'django.contrib.auth', # AUTH (LOGIN & SIGN UP): Default Authentication Backend Used By Django. Application Allows For The Creation Of Users.
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "main.apps.MainConfig", # MAIN: Models, Views Etc. Found Within 'main' Can Be Used. I Have Developed This Application.
    "register.apps.RegisterConfig", # REGISTER: Models, Views Etc. Found Within 'register' Can Be Used. I Have Developed This Application.
    "crispy_forms", # CRISPY_FORMS: Crispy Styling Can Be Used On Forms To Make Them Look Aesthetically Pleasing. Has To Be Installed Via PIP.
    "django_filters", # DJANGO_FILTERS: Include 'django_filters' Package To Be Used So There Is A Filter System. Has To Be Installed Via PIP.
]

# FORM STYLING: Configure CSS Framework 'crispy_forms' Will Make Use Of.
CRISPY_TEMPLATE_PACK = "bootstrap4"
# LOGIN MADE: Once A User Has Logged In And Been Authenticated Redirect Them To The Specified URL.
LOGIN_REDIRECT_URL = "/home"
# LOGOUT MADE: Once A User Has Logged Out Redirect Them To The Specified URL.
LOGOUT_REDIRECT_URL = "/logout"

# SMTP CONFIGURATION: Settings Required To Send Emails With Django.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "kamalabdulhafiz@gmail.com"
EMAIL_HOST_PASSWORD = "rtypgxuyqfmdqwfr" # APP PASSWORD: App Password Has Been Set Up In Gmail.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ExpenseTracker.urls'

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

WSGI_APPLICATION = 'ExpenseTracker.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASE CONFIGURATION: SQLITE3 Will Be Shown In Directory Once Initial Migration Has Been Made And Can Be Made Use Of.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = "home/akamalah/ExpenseTracker/static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
