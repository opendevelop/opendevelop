from django.http import HttpResponse
import json

class JSONResponse(HttpResponse):
    def __init__(self, content={}, content_type='application/json', status=200):
        types = [dict, list, tuple]
        if (type(content) in types):
            content = json.dumps(content)
        super(JSONResponse, self).__init__(content, content_type, status)
