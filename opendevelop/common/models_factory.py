import factory
import models

def prefix_seq(x):
    return lambda n : x + '-{0}'.format(n)

class OpenDevelopUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.OpenDevelopUser
    username = factory.Sequence(prefix_seq('username'))
