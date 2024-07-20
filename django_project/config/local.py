from .base import *  # noqa: F403
from .base import env

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY", default="localrunsecret")

ALLOWED_HOSTS = "localhost", "0.0.0.0", "127.0.0.1"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)


# for debug toolbar setting
INTERNAL_IPS = [  # noqa: F405
    "127.0.0.1",
]

# INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS

# MIDDLEWARE += [  # noqa: F405
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

# MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
#     "SHOW_TEMPLATE_CONTEXT": True,
# }


ADMIN_URL = "ov-admin/"

# STORAGE["staticfiles"][  # noqa F405
#     "BACKEND"
# ] = "whitenoise.storage.CompressedManifestStaticFilesStorage"
