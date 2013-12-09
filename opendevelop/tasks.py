from celery import Celery
import os
import time

app = Celery('tasks', broker='amqp://guest@localhost', backend='amqp')


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
    binds = {
                '/data': directory
            }
    sandbox.docker_server.start(container_id, binds)
    return "created container"
