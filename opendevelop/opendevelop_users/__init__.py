from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import App, OpenDevelopUser

admin.site.register(App)
admin.site.register(OpenDevelopUser, UserAdmin)
