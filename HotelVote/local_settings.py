DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotel',
        'USER': 'root',
        'PASSWORD': 'manish94',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#if using sendmail binary to send emails, uncomment the following
#EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

#if using SMTP server to send emails
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'admin@hotel.com'
