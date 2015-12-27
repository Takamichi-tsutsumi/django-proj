#
# import os

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# TEMPLATE_DEBUG = True
#
# ALLOWED_HOSTS = []
#
#
# # Application definition
#
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )
#
# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django_socketio',
#     'bootstrapform', # django-bootstrap-form
#     'cms',
#     'simpleboard',
#     'websock',
# )
#
# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )
#
# ROOT_URLCONF = 'myboard.urls'
#
# WSGI_APPLICATION = 'myboard.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'myboard',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '',
#         'PORT': '',
#     }
# }
#
# # Internationalization
# # https://docs.djangoproject.com/en/1.7/topics/i18n/
#
# LANGUAGE_CODE = 'utf-8'
#
# TIME_ZONE = 'Asia/Tokyo'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = False
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.7/howto/static-files/
#
# STATIC_URL = '/static/'
# #
# # LOGGING = {
# #     'version': 1,
# #     'disable_existing_loggers': False,
# #     'handlers': {
# #         'console': {
# #             'level': 'DEBUG',
# #             'class': 'logging.StreamHandler',
# #         },
# #     },
# #     'loggers': {
# #         'django': {
# #             'handlers': ['console'],
# #             'level': 'DEBUG',
# #         },
# #     },
# # }
#

# #
# # LOGIN_URL = '/simpleboard/login/'
# #
# # LOGIN_REDIRECT_URL = '/simpleboard/'
#
# TEMPLATE_CONTEXT_PROCESSORS = {
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.request',
# }
#


import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '9=2dvu0&*418zo@)-ik_rqjyt_oc50v-!ie7615_mx(y$bg18z'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = PROJECT_ROOT.split(os.sep)[-1]

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
full_path = lambda *parts: os.path.join(PROJECT_ROOT, *parts)
example_path = full_path("..", "..")
if example_path not in sys.path:
    sys.path.append(example_path)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_URL = "/static/"
ROOT_URLCONF = "%s.urls" % PROJECT_DIR
TEMPLATE_DIRS = list(full_path("templates"))
#LOGIN_URL = "/admin/"

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django_socketio',
    'websock',
)


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}