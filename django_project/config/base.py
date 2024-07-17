from django.contrib.messages import constants as messages

from pathlib import Path
import environ
import locale
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # jalali
    "django_jalali",
    # server
    "daphne",
    # cms
    # "djangocms_admin_style",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.flatpages",
    # cms
    #     "cms",
    #     "menus",
    #     "treebeard",
    #     "sekizai",
    #     "djangocms_alias",
    #     "filer",
    #     "easy_thumbnails",
    #     "djangocms_text_ckeditor",
    #     "djangocms_frontend",
    #     "djangocms_frontend.contrib.accordion",
    #     "djangocms_frontend.contrib.alert",
    #     "djangocms_frontend.contrib.badge",
    #     "djangocms_frontend.contrib.card",
    #     "djangocms_frontend.contrib.carousel",
    #     "djangocms_frontend.contrib.collapse",
    #     "djangocms_frontend.contrib.content",
    #     "djangocms_frontend.contrib.grid",
    #     "djangocms_frontend.contrib.image",
    #     "djangocms_frontend.contrib.jumbotron",
    #     "djangocms_frontend.contrib.link",
    #     "djangocms_frontend.contrib.listgroup",
    #     "djangocms_frontend.contrib.media",
    #     "djangocms_frontend.contrib.tabs",
    #     "djangocms_frontend.contrib.utilities",
    # htmx
    "django_htmx",
    # local
    "accounts",
    "pages",
    # phone number
    "phonenumber_field",
    # allauth
    "allauth",
    "allauth.account",
]


MIGRATION_MODULES = {"sites": "contrib.sites.migrations"}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    # "cms.middleware.user.CurrentUserMiddleware",
    # "cms.middleware.page.CurrentPageMiddleware",
    # "cms.middleware.toolbar.ToolbarMiddleware",
    # "cms.middleware.language.LanguageCookieMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                # "sekizai.context_processors.sekizai",
                # "cms.context_processors.cms_settings",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# WSGI_APPLICATION = "django_project.wsgi.application"
ASGI_APPLICATION = "django_project.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_NAME", default="postgres"),
        "USER": env.str("POSTGRES_USER", default="postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="postgres"),
        "HOST": env.str("POSTGRES_HOST", default="localhost"),
        "PORT": "5432",
    }
}
# DATABASES["default"]["ATOMIC_REQUESTS"] = True


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
PASSWORD_HASHERS = ("django.contrib.auth.hashers.Argon2PasswordHasher",)

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [str(BASE_DIR / "static")]
STORAGE = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# user
AUTH_USER_MODEL = "accounts.CustomUser"

# MESSAGES
MESSAGE_TAGS = {
    messages.DEBUG: "secondary m-1",
    messages.INFO: "info m-1",
    messages.SUCCESS: "success m-1",
    messages.WARNING: "warning m-1",
    messages.ERROR: "danger m-1",
}

# logger
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

LANGUAGES = [("fa", "Persian")]

# auth
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# login
LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "posts:post_list"
LOGOUT_REDIRECT_URL = "logged_out"

ACCOUNT_SIGNUP_PASSWORD_TWICE = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True


ADMIN_URL = "admin/"

# cms
# CMS_CONFIRM_VERSION4 = True
# CMS_TEMPLATES = [
#     ("pages/home.html", "Home page template")
# ]
# THUMBNAIL_HIGH_RESOLUTION = True
# THUMBNAIL_PROCESSORS = (
#     'easy_thumbnails.processors.colorspace',
#     'easy_thumbnails.processors.autocrop',
#     'filer.thumbnail_processors.scale_and_crop_with_subject_location',
#     'easy_thumbnails.processors.filters'
# )

# x frame
X_FRAME_OPTIONS = "SAMEORIGIN"

# phone number
PHONENUMBER_DEFAULT_REGION = "IR"

# jalali date
locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
