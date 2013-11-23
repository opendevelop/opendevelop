from common.views import JSONResponse
from common import utils
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from common.decorators import oauth
from django.views.generic import View
from models import Sandbox
from images.models import Image
import logic


class SandboxListView(View):

    @oauth
    def get(self, request, **kwargs):
        sandboxes = Sandbox.objects.filter(owner_app=request.app)
        sandboxes_dict = [sandbox_to_dict(s) for s in sandboxes]
        return JSONResponse(content={'sandboxes': sandboxes_dict})

    @oauth
    def post(self, request):
        try:
            data = utils.get_request_dict(request)
        except Exception as e:
            return HttpResponseBadRequest(e.args)
        try:
            cmd = data['cmd']
            image_id = data['image_id']
        except KeyError:
            return HttpResponseBadRequest("Command or image_id missing")
        try:
            image = Image.objects.get(slug=image_id)
        except Image.DoesNotExist:
            return HttpResponseNotFound("No image found")
        try:
            f = request.FILES['file']
        except:
            f = None
        sandbox_id = logic.create(request.app, cmd, image, f)
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
