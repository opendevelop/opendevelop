from common.views import JSONResponse
from django.http import HttpResponseNotFound
from common.decorators import oauth
from django.views.generic import View
from models import Sandbox
import logic


class SandboxListView(View):

    @oauth
    def get(self, request, **kwargs):
        sandboxes = Sandbox.objects.filter(owner_app=request.app)
        sandboxes_dict = [sandbox_to_dict(s) for s in sandboxes]
        return JSONResponse(content={'sandboxes': sandboxes_dict})

    @oauth
    def post(self, request):
        sandbox_id = logic.create()
        return JSONResponse(content={'sandbox_id': sandbox_id})


class SandboxSingleView(View):

    @oauth
    def get(self, request, sandbox_id):
        try:
            sandbox = Sandbox.objects.get(id=sandbox_id)
        except Sandbox.DoesNotExist:
            return HttpResponseNotFound("SandBox not found")
        sbx_dict = sandbox_to_dict(sandbox)
        return JSONResponse(content=sbx_dict)


def sandbox_to_dict(sandbox):
    d = {}
    d['image'] = sandbox.image.id
    d['cmd'] = sandbox.cmd
    d['status'] = sandbox.status
    try:
        d['return_code'] = sandbox.log.return_code
        d['logs'] = sandbox.log.logs
    except:
        d['return_code'] = None
        d['logs'] = None
    return d
