from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db.models import Q
from opendevelop_users import models
import re


class Command(BaseCommand):

    help = "Add a new Opendevelop App"

    option_list = BaseCommand.option_list + (
        make_option(
            '--username',
            dest='username',
            help="Specify a username to associate the app with"),
        make_option(
            '--email',
            dest='email',
            help="Specify a user mail-address to assosiacte the app with"),
        make_option(
            '--app_name',
            dest='app_name',
            help="Name for the new app"),
    )

    def handle(self, *args, **options):
        username = options['username']
        mail = options['email']
        app_name = options['app_name']

        if username is None and mail is None:
            raise CommandError("Please give a username or an email")

        if app_name is None:
            raise CommandError("Please provide a name for the app")

        try:
            user = models.OpenDevelopUser.objects.get(Q(username=username) |
                                                      Q(email=mail))
        except models.OpenDevelopUser.DoesNotExist:
            raise CommandError("User not found")

        app = models.App.objects.create(name=app_name, owner=user)

        self.stdout.write("An app created succesfully\n"
                          "Client ID %s\nClient Secret %s\n"
                          % (app.client_id, app.client_secret))
