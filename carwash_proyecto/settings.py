"""
Django settings for carwash_proyecto project.
Optimized for Render.com deployment.
"""

import os
from pathlib import Path

# 1. DIRECTORIO RAÍZ
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. SEGURIDAD (En producción, usa Variables de Entorno para la SECRET_KEY)
SECRET_KEY = 'django-insecure-b_kh&nf8o7o0z$q23v1b+d^bsa^!r7hmf(26vush$&1s7ysj4w'

# Mantenemos DEBUG en True para ver errores si algo falla, cámbialo a False al terminar.
DEBUG = True

# Permitimos todos los hosts para evitar errores de conexión en Render
ALLOWED_HOSTS = ['*']


# 3. DEFINICIÓN DE APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'turnos', # Tu aplicación de turnos
]

# 4. MIDDLEWARE (WhiteNoise debe ir después de SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # SERVIDOR DE ARCHIVOS ESTÁTICOS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carwash_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'carwash_proyecto.wsgi.application'


# 5. BASE DE DATOS (SQLite por defecto)
# Nota: Los datos se borrarán en cada reinicio de Render con SQLite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 6. VALIDACIÓN DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 7. INTERNACIONALIZACIÓN
LANGUAGE_CODE = 'es-cl' # Cambiado a español de Chile
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True


# 8. ARCHIVOS ESTÁTICOS (EL ARREGLO PARA RENDER)
STATIC_URL = '/static/'

# Carpeta donde se recolectarán los archivos para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración de WhiteNoise para almacenamiento eficiente
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# 9. OTROS AJUSTES
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
