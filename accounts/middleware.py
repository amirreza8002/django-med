from django.contrib.auth.middleware import auser, get_user
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject


class AsyncAuthenticationMiddleware(MiddlewareMixin):
    async def __acall__(self, request):
        response = None
        if hasattr(self, "process_request"):
            response = await self.process_request(request)
        response = response or await self.get_response(request)

        if hasattr(self, "process_response"):
            response = await self.process_response(request)

        return response

    async def process_request(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The Django authentication middleware requires session "
                "middleware to be installed. Edit your MIDDLEWARE setting to "
                "insert "
                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                "'django.contrib.auth.middleware.AuthenticationMiddleware'."
            )

        request.user = SimpleLazyObject(lambda: get_user(request))
        request.auser = await auser(request)
