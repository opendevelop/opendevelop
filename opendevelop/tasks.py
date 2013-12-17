"""
This module should handle all the asynchronous tasks
of OpenDevelop.
"""

from __future__ import absolute_import
from celery import Celery
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
import json
import os
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opendevelop.settings')
from sandboxes.models import Sandbox

CELERY_ACCEPT_CONTENT = ['json']
app = Celery('opendevelop',
             broker='amqp://guest@localhost',
             backend='amqp')
app.config_from_object('django.conf:settings')


def create_script(commands):
    template = get_template("start.sh")
    print commands
    c = Context({'commands': commands[:-1], 'last_cmd': commands[-1]})
    return template.render(c)


@app.task
def run_code(sandbox, cmd, files):
    """
    This function is supposed to
     1. Create the sandbox bucket
     2. Create the sandbox container
     3. Start the sandbox container
    """
    directory = '/etc/opendevelop/buckets/%s/' % sandbox.id
    data_dir = directory + "data/"
    os.makedirs(data_dir)
    for key, val in files.iteritems():
        with open(data_dir+key, 'wb+') as destination:
            for chunk in val.chunks():
                destination.write(chunk)

    with open(directory+"start", 'w') as script:
        script.write(create_script(cmd))

    img = sandbox.image.docker_image_name
    volumes = {
        '/var/opendevelop/bucket': {}
        }
    docker_cmd = "bin/sh /var/opendevelop/bucket/start"
    try:
        client = sandbox.docker_server.api
        container_id = client.create_container(image=img,
                                               command=docker_cmd,
                                               volumes=volumes)
    except Exception as e:
        raise e

    sandbox.container_id = container_id['Id']
    sandbox.save()
    binds = {
        directory: '/var/opendevelop/bucket'
        }
    client.start(container_id, binds)
    return "created container"
