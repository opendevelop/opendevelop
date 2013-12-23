from django.utils import simplejson as json


def get_request_dict(request):
    """Return data sent by the client as python dictionary.
        Only JSON format is supported
    """
    data = request.body
    content_type = request.META.get("CONTENT_TYPE")
    if content_type is None:
        raise Exception("Missing Content-Type header field")
    if content_type.startswith("application/json"):
        try:
            return json.loads(data)
        except ValueError:
            raise Exception("Invalid JSON data")
    else:
        raise Exception("Unsupported Content-type: '%s'" % content_type)
