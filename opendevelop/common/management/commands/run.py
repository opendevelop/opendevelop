from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.runserver import Command as Runserver
import sys

class Command(BaseCommand):
    help = 'Starts the opendevelop server'
    def handle(self, *args, **options):
        runserver = Runserver()
        runserver.stdout = sys.stdout
        runserver.handle('0.0.0.0:8000', *args, **options)
