from common.views import JSONResponse
from common.decorators import oauth
from django.views.generic import View
from models import Sandbox

class SandboxListView(View):

    @oauth
    def get(self, request, **kwargs):
        return JSONResponse([])
