import factory

import models

from opendevelop_users import models_factory as app_mf
from images import models_factory as image_mf


class SandboxFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Sandbox
    owner_app = app_mf.AppFactory()
    image = factory.SubFactory(image_mf.ImageFactory)
