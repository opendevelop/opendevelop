from celery import Celery
import os
import time

app = Celery('tasks', broker='amqp://guest@localhost', backend='amqp')


@app.task
def run_code(sandbox_id, cmd, files):
    directory = '/etc/opendevelop/buckets/%s/' % sandbox_id
    os.mkdir(directory)
    for key, val in files.iteritems():
        with open(directory+key, 'wb+') as destination:
            for chunk in val.chunks():
                destination.write(chunk)
    # call to the docker api
    return "created container"
