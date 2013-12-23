from .models import Sandbox, SandboxLog
from common.models import DockerServer
from images.models import Image
import json
import tasks


def create(app, cmd, image, files):
    docker_server = DockerServer.objects.order_by('?')[0]
    sandbox = Sandbox.objects.create(owner_app=app, cmd=json.dumps(cmd),
                                     image=image,
                                     docker_server=docker_server,
                                     status='running')
    r = tasks.run_code.delay(sandbox, cmd, files)
    return sandbox


def fetch_logs(sandbox):
    client = sandbox.docker_server.api
    try:
        sandbox.log
    except SandboxLog.DoesNotExist:
        SandboxLog.objects.create(sandbox=sandbox)
    sandbox.log.logs = client.logs(sandbox.container_id)
    container = client.inspect_container(sandbox.container_id)
    if not container['State']['Running']:
        sandbox.log.return_code = container['State']['ExitCode']
        sandbox.status = 'terminated'
    sandbox.log.save()
    sandbox.save()
