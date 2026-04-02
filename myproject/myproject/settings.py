from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔥 DEBUG MODE
DEBUG = True

# 🔥 HOSTS
ALLOWED_HOSTS = []

# 🔐 SECRET KEY
SECRET_KEY = 'django-insecure-change-this-key'

# 📦 INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',   # 🔥 ADD THIS
    'users',
]

# ⚙️ MIDDLEWARE (CORS MUST BE FIRST 🔥)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 🔥 ADD THIS ON TOP

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# 🔗 URL CONFIG
ROOT_URLCONF = 'myproject.urls'

# 🎨 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# 🚀 WSGI
WSGI_APPLICATION = 'myproject.wsgi.application'

# 🗄️ DATABASE (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'Jaga@1439',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 🔑 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]

# 🌍 LANGUAGE & TIME
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# 📁 STATIC FILES
STATIC_URL = 'static/'

# 🔢 DEFAULT FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔐 LOGIN REDIRECT
LOGIN_URL = '/login/'

# 🔥🔥 CORS FIX (VERY IMPORTANT)
CORS_ALLOW_ALL_ORIGINS = True