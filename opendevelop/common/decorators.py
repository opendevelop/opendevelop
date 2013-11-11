from common.views import HttpResponseUnauthorized
from functools import wraps

def oauth(view):
    @wraps(view)
    def wrapper(self, request, **kwargs):
        AUTH_HEADER_KEY = 'HTTP_AUTHORIZATION'
        if (not AUTH_HEADER_KEY in request.META):
            msg = 'This resource requires OAuth2 authorization.'
            return HttpResponseUnauthorized(msg)
        return view(self, request, **kwargs)
    return wrapper
