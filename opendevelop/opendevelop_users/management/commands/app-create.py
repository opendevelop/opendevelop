from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db.models import Q
from opendevelop_users import models
import re


class Command(BaseCommand):

    help = "Add a new Opendevelop user"

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

        try:
            user = models.OpenDevelopUser.objects.get(Q(username=username) |
                                                      Q(email=mail))
        except models.OpenDevelopUser.DoesNotExist:
            raise CommandError("User not found")
