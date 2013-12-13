from models import Sandbox
from common.models import DockerServer
from images.models import Image
import tasks


def create(app, cmd, image, files):
    docker_server = DockerServer.objects.order_by('?')[0]
    sandbox = Sandbox.objects.create(owner_app=app, cmd=cmd, image=image,
                                     docker_server=docker_server)
    r = tasks.run_code.delay(sandbox, cmd, files)
    return sandbox
