from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from api import models
import re


class Command(BaseCommand):

    help = "Add a new Opendevelop user"

    option_list = BaseCommand.option_list + (
        make_option(
            '--username',
            dest='username',
            help="Specify a username"),
        make_option(
            '--email',
            dest='email',
            help="Specify a valid email-address"),
        make_option(
            '--passwd',
            dest='passwd',
            help="Specify a password up to 20 chars"),
        make_option(
            '--organization',
            dest='organization',
            action='store_true',
            default=False,
            help="Is this user an organization"),
    )

    def handle(self, *args, **options):
        username = options['username']
        mail = options['email']
        passwd = options['passwd']
        is_org = options['organization']

        if username is None or mail is None or passwd is None:
            raise CommandError("Missing Data")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            raise CommandError("Wrong email address")

        if len(passwd) > 20:
            raise CommandError("Too long password")

        user = models.OpenDevelopUser.objects.create(username=username,
                                                     email=mail,
                                                     password=passwd,
                                                     is_organization=is_org)

        self.stdout.write("New user %s created succesfully" % username)
