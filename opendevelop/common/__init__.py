from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import DockerServer
from models import OpenDevelopUser
from os import makedirs
from subprocess import call
from subprocess import PIPE

admin.site.register(DockerServer)
admin.site.register(OpenDevelopUser, UserAdmin)


def cmd(args):
    return call(args, stdout=PIPE, stderr=PIPE)


def mkdir(path):
    makedirs(path)
    cmd(['chmod', 'g+rwx', path])
