import factory
from models import App
from common import models_factory as cmf
from random import choice
from string import digits, letters

def random_string(x):
    return ''.join(choice(digits+letters) for x in range(x))

class AppFactory(factory.DjangoModelFactory):
    FACTORY_FOR = App
    client_id = factory.Sequence(lambda self : random_string(20))
    client_secret = factory.Sequence(lambda self : random_string(40))
    owner = cmf.OpenDevelopUserFactory()
