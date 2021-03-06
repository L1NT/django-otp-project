from os.path import dirname, join, abspath


def project_path(path):
    return abspath(join(dirname(__file__), path))


USE_TZ = True

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django_otp',
    'django_otp.plugins.otp_hotp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_email',

    'otp_yubikey',
    'otp_twilio',

    'django_agent_trust',
    'otp_agents',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django_agent_trust.middleware.AgentMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_DIRS = [
    project_path('templates'),
]

SECRET_KEY = 'cI4AHyAcIKQxcq2hI54YS7Bnn6vbojTxxlTWQdRiA2pky5oz8IEgJ1DcyvCDXnXn'

ROOT_URLCONF = 'urls'
