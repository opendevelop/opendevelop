from common.views import HttpResponseUnauthorized
from functools import wraps
import base64

def oauth(view):
    @wraps(view)
    def wrapper(self, request, **kwargs):
        AUTH_HEADER_KEY = 'HTTP_AUTHORIZATION'
        if (not AUTH_HEADER_KEY in request.META):
            msg = 'This resource requires OAuth2 authorization.'
            return HttpResponseUnauthorized(msg)
        auth_data = base64.standard_b64decode(request.META[AUTH_HEADER_KEY])
        return view(self, request, **kwargs)
    return wrapper
