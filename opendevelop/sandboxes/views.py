from common.views import JSONResponse
from common.decorators import oauth
from django.views.generic import View
from models import Sandbox
import logic

class SandboxListView(View):

    #@oauth
    def get(self, request, **kwargs):
        return JSONResponse([])

    def post(self, request):
        sandbox_id = logic.create()
        return JSONResponse(content={'sandbox_id': sandbox_id})

class SandboxSingleView(View):

    @oauth
    def get(self, request, sandbox_id):
        d = {"test": sandbox_id}
        return JSONResponse(content=d)
