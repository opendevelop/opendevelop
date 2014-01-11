from django.contrib import admin
from models import DockerServer
from os import makedirs
from subprocess import call
from subprocess import PIPE

admin.site.register(DockerServer)

def cmd(args):
    return call(args, stdout=PIPE, stderr=PIPE)


def mkdir(path):
    makedirs(path)
    cmd(['chmod', 'g+rwx', path])
