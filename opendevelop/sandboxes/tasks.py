"""
This module should handle all the asynchronous tasks
of OpenDevelop.
"""

from __future__ import absolute_import
from celery import shared_task
from django.template.loader import get_template
from django.template import Context
from sandboxes.models import Sandbox
import json
import os
import time


def create_script(commands):
    template = get_template('start.sh')
    c = Context({'commands': commands[:-1], 'last_cmd': commands[-1]})
    return template.render(c)


@shared_task
def run_code(sandbox, cmd, files):
    """
    This function is supposed to
    1. Create the sandbox bucket
    2. Create the sandbox container
    3. Start the sandbox container
    """
    directory = '/etc/opendevelop/buckets/%s/' % sandbox.id
    data_dir = directory + 'data/'
    os.makedirs(data_dir)
    for key, val in files.iteritems():
        with open(data_dir+key, 'wb+') as destination:
            for chunk in val.chunks():
                destination.write(chunk)

    with open(os.path.join(directory, 'start'), 'w') as script:
        script.write(create_script(cmd))

    img = sandbox.image.docker_image_name
    volumes = {
               '/var/opendevelop/bucket': {}
        }
    docker_cmd = '/bin/sh /var/opendevelop/bucket/start'
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
    return container_id['Id']

@shared_task
def kill_sandb(c_id,timeout):
    try:
        sandbox=Sandbox.objects.get(container_id=c_id)
        client=sandbox.docker_server.api
        time.sleep(int(timeout))
        client.kill(sandbox.container_id)
    except Exception as e:
        raise e
    return True
