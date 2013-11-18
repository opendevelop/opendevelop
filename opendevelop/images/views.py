from common.views import JSONResponse
from django.views.generic import View
from models import Image


class ImagesView(View):
    def get(self, request):
        images = Image.objects.all()
        slugs = []
        for image in images:
            slugs.append(image.slug)
        return JSONResponse(slugs)
