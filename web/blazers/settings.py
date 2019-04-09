import blazers

# if blazers.db.env.IsDjangoDebugEnabled():
#     DEBUG = True
#     ALLOWED_HOSTS = ['*']
# else:
#     CSRF_COOKIE_HTTPONLY = False
#     CSRF_COOKIE_SECURE   = False
#     SESSION_COOKIE_SECURE = True
#     DEBUG = False
#     ALLOWED_HOSTS = ['*']

DEBUG = True

import os
projectFolder = os.path.dirname(__file__)


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '/tmp/sqlite.db',                      # Or path to database file if using sqlite3.
#         'USER': 'nobody',                      # Not used with sqlite3.
#         'PASSWORD': 'pw',                  # Not used with sqlite3.
#         'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

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
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = ''


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
# STATIC_URL = 'https://static.apervita.net/' # deployed env setting

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(projectFolder, '..', '..', 'static'),
    # os.path.join('/opt/apervita', 'apervita', 'static'), # deployed env setting
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
#    'compressor.finders.CompressorFinder',
)

# STATICFILES_STORAGE = 'require.storage.OptimizedCachedStaticFilesStorage' # deployed env setting

# REQUIRE_BASE_URL = 'js'
# REQUIRE_BUILD_PROFILE = 'app.build.js'
# REQUIRE_JS = os.path.join('src', 'require.js')
# REQUIRE_ENVIRONMENT = 'node'
# # REQUIRE_ENVIRONMENT = 'lib.helpers.statichelpers.NodeEnvironment' # for collect static locally
# REQUIRE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'secret_key'

ROOT_URLCONF = 'blazers.urls'
SESSION_SAVE_EVERY_REQUEST = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(projectFolder, '..', 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',

                # Default Django Config
                'django.template.context_processors.debug',  # comment out in deployed env
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ]
        },
    },
]

INTERNAL_IPS = ('localhost', '127.0.0.1')
