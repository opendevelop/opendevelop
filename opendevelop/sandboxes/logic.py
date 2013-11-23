from models import Sandbox
import tasks


def create(app, cmd, image, files):
    sandbox = Sandbox.objects.create(status=Sandbox.CREATED, owner_app=app,
                                     cmd=str(cmd), image=image)
    r = tasks.run_code.delay(sandbox.id, cmd, files)
    return sandbox.id
