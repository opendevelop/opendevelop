import factory
from api.models import App, OpenDevelopUser
from random import choice
from string import digits, letters


def random_string(x):
    return ''.join(choice(digits+letters) for x in range(x))


def prefix_seq(x):
    return lambda n: x + '-{0}'.format(n)


class OpenDevelopUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = OpenDevelopUser
    username = factory.Sequence(prefix_seq('username'))
    email = factory.Sequence(prefix_seq('email'))


class AppFactory(factory.DjangoModelFactory):
    FACTORY_FOR = App
    client_id = factory.Sequence(lambda self: random_string(20))
    client_secret = factory.Sequence(lambda self: random_string(40))
    owner = factory.SubFactory(OpenDevelopUserFactory)
