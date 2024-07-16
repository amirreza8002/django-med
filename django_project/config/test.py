from .base import *  # noqa F403
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY", default="testsecretkey")
DEBUG = True

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

TEST_RUNNER = "django.test.runner.DiscoverRunner"

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

TEMPLATES[0]["OPTIONS"]["debug"] = True  # noqa F405

MEDIA_URL = "http://media.testserver"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_NAME", default="postgres"),
        "USER": env.str("POSTGRES_USER", default="postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="postgres"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}
