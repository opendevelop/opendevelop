from common.views import HttpResponseUnauthorized
from django.http import HttpResponseBadRequest
from functools import wraps
import base64

def oauth(view):
    @wraps(view)
    def wrapper(self, request, **kwargs):
        AUTH_HEADER_KEY = 'HTTP_AUTHORIZATION'
        if (not AUTH_HEADER_KEY in request.META):
            msg = 'This resource requires OAuth2 authorization.'
            return HttpResponseUnauthorized(msg)
        auth_header = request.META[AUTH_HEADER_KEY]
        try:
            auth_data = base64.standard_b64decode(auth_header)
            auth_data = auth_data.split(':')
            if (len(auth_data) <> 2):
                raise Exception()
        except Exception:
            return HttpResponseBadRequest('Invalid Authorization header data.')
        return view(self, request, **kwargs)
    return wrapper
