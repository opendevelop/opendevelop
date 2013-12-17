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
import json


class SandboxListView(View):
    """
    This class handles the listing and creation of sandboxes.
    """

    @oauth
    def get(self, request, **kwargs):
        """
        Returns the list of sandboxes owned by the currently authenticated app.
        """
        sandboxes = Sandbox.objects.filter(owner_app=request.app)
        sandboxes_dict = [s.to_dict() for s in sandboxes]
        return JSONResponse({'sandboxes': sandboxes_dict})

    @oauth
    def post(self, request):
        """
        Creates a new sandbox for the currently authenticated app.
        """

        data = request.POST
        try:
            cmd = data['cmd']
            image = data['image']
        except (ValueError, KeyError):
            return HttpResponseBadRequest("Command or image slug missing")

        try:
            commands = json.loads(cmd)
        except ValueError:
            commands = [cmd]
        except KeyError:
            return HttpResponseBadRequest("Malformed cmd field")
        
        if (not (type(commands)) == list):
            return HttpResponseBadRequest("Malformed cmd field")

        try:
            image = Image.objects.get(slug=image)
        except:
            return HttpResponseBadRequest("No image found")
        files = request.FILES
        sandbox = logic.create(request.app, commands, image, files)
        return JSONResponse(sandbox.slug)


class SandboxSingleView(View):
    """
    This view handles the inspection of a single sandbox.
    """

    @oauth
    def get(self, request, sandbox_slug):
        """
        Returns information about a specific sandbox
        owned by the currently authenticated app and identified
        by the given sandbox_slug
        """
        try:
            sandbox = Sandbox.objects.get(slug=sandbox_slug)
        except Sandbox.DoesNotExist:
            return HttpResponseNotFound("SandBox not found")
        if sandbox.status != 'terminated':
            logic.fetch_logs(sandbox)
        sandbox_dict = sandbox.to_dict()
        return JSONResponse(content=sandbox_dict)
