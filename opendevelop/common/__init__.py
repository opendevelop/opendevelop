from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import DockerServer
from models import OpenDevelopUser

admin.site.register(DockerServer)
admin.site.register(OpenDevelopUser, UserAdmin)
