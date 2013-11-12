from common.views import HttpResponseUnauthorized
from django.http import HttpResponseBadRequest
from functools import wraps
import base64

def oauth(view):
    @wraps(view)
    def wrapper(self, request, **kwargs):
        ALLOWED_BEARER_TYPES = ['Basic']
        AUTH_HEADER_KEY = 'HTTP_AUTHORIZATION'

        if (not AUTH_HEADER_KEY in request.META):
            msg = 'This resource requires OAuth2 authorization.'
            return HttpResponseUnauthorized(msg)
        auth_header = request.META[AUTH_HEADER_KEY]

        try:
            (bearer_type, auth_data) = tuple(auth_header.split(' '))
            if (not bearer_type in ALLOWED_BEARER_TYPES):
                bearers = ', '.join(ALLOWED_BEARER_TYPES)
                msg = 'Incorrect bearer type. Available types: %s' % bearers
                return HttpResponseBadRequest(msg)
            auth_data = base64.standard_b64decode(auth_data)
            (client_id, client_secret) = tuple(auth_data.split(':'))
        except Exception:
            return HttpResponseBadRequest('Invalid Authorization header data.')

        if (len(client_id) <> 20):
            return HttpResponseBadRequest('client_id should be 20 chars long.')

        if (len(client_secret) <> 40):
            return HttpResponseBadRequest('client_secret should be 40 chars long.')

        return view(self, request, **kwargs)
    return wrapper
