"""
This module contains class based views that deal with
either multiple or single sandboxes. All of the views require
oAuth authentication
"""

from common.views import JSONResponse
from common import utils
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from common.decorators import oauth
from django.views.generic import View
from models import Sandbox
from images.models import Image
import logic


class SandboxListView(View):
    """
    This class handles the views that have to do with
    multiple sandboxes.
    """

    @oauth
    def get(self, request, **kwargs):
        """
        Returns the list of sandboxes owned by the
        currently authenticated app.
        """
        sandboxes = Sandbox.objects.filter(owner_app=request.app)
        sandboxes_dict = [s.to_dict() for s in sandboxes]
        return JSONResponse({'sandboxes': sandboxes_dict})


class SandboxSingleView(View):
    """
    This view handles the inspection and creation of
    a single sandbox.
    """

    @oauth
    def get(self, request, sandbox_id):
        """
        Returns information about a specific sandbox
        owned by the currently authenticated app and identified
        by the given sandbox_id
        """
        try:
            sandbox = Sandbox.objects.get(pk=sandbox_id)
        except Sandbox.DoesNotExist:
            return HttpResponseNotFound("SandBox not found")
        sandbox_dict = sandbox.to_dict()
        return JSONResponse(content=sandbox_dict)

    @oauth
    def post(self, request):
        """
        Creates a new sandbox for the currently authenticated app.
        """
        data = request.POST
        try:
            cmd = data['cmd']
            image_id = data['image_id']
        except KeyError:
            return HttpResponseBadRequest("Command or image_id missing")
        try:
            image = Image.objects.get(pk=image_id)
        except:
            return HttpResponseBadRequest("No image found")
        files = request.FILES
        sandbox_id = logic.create(request.app, cmd, image, files)
        return JSONResponse({'sandbox_id': sandbox_id})
