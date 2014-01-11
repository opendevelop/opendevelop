from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

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
                help="Is this user an organization"),
    )

    def handle(self, *args, **options):

