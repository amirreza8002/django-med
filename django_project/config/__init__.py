from .base import *

level = env.str("DJANGO_LEVEL", default="dev")  # noqa F405

if level == "prod":
    from .production import *
else:
    from .local import *
