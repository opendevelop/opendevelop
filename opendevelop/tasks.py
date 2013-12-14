"""
This module should handle all the asynchronous tasks
of OpenDevelop.
"""

from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opendevelop.settings')
from sandboxes.models import Sandbox

app = Celery('opendevelop',
             broker='amqp://guest@localhost',
             backend='amqp')
app.config_from_object('django.conf:settings')

@app.task
def run_code(sandbox, cmd, files):
	"""
	This function is supposed to
	  1. Create the sandbox bucket
	  2. Create the sandbox container
	  3. Start the sandbox container
	"""
    directory = '/etc/opendevelop/buckets/%s/' % sandbox.id
    os.mkdir(directory)
    for key, val in files.iteritems():
        with open(directory+key, 'wb+') as destination:
            for chunk in val.chunks():
                destination.write(chunk)
    img = sandbox.image.docker_image_name
    volumes = {
                '/data': {}
              }
    try:
        container_id = sandbox.docker_server.api.create_container(image=img,
                                                                  command=cmd,
                                                                  volumes=volumes
                                                                 )
    except Exception as e:
        print dir(e)
        print dir(e.response)
        print e.response.url
        print e.response.content
        raise e

    sandbox.container_id = container_id
    sandbox.save()
    binds = {
                directory: '/data'
            }
    sandbox.docker_server.start(container_id, binds)
    return "created container"
