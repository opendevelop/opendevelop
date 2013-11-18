import factory
import models
from api import models_factory as api_mf
from images import models_factory as image_mf

class SandboxFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Sandbox
    owner_app = api_mf.AppFactory()
    image = factory.SubFactory(image_mf.ImageFactory)
