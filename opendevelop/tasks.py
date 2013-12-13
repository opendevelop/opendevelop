from celery import Celery
from django.conf import settings
import os
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opendevelop.settings')

app = Celery('opendevelop', broker='amqp://guest@localhost', backend='amqp')
app.config_from_object('django.conf:settings')

@app.task
def run_code(sandbox, cmd, files):
    directory = '/etc/opendevelop/buckets/%s/' % sandbox_id
    os.mkdir(directory)
    for key, val in files.iteritems():
        with open(directory+key, 'wb+') as destination:
            for chunk in val.chunks():
                destination.write(chunk)
    img = sandbox.image.docker_image_name
    volumes = {
                '/data': {}
              }
    container_id = sandbox.docker_server.create_container(
                                                            image=img,
                                                            command=cmd,
                                                            volumes=volumes
                                                         )
    sandbox.container_id = container_id
    sandbox.save()
    binds = {
                '/data': directory
            }
    sandbox.docker_server.start(container_id, binds)
    return "created container"
