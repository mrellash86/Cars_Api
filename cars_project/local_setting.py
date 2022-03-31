# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#dbz1t=w^4+0*(9&og58sxo=_lw(j^ck^b#mdlf^9#8!35f6p!'
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}