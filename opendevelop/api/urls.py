from django.conf.urls import patterns, include, url

from images.views import ImagesView

urlpatterns = patterns('',
    url(r'^images/', ImagesView.as_view()),
)
