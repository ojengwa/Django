from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'circle_test',
#         'USER': 'ubuntu',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         'TEST_NAME': 'circle_test',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}