from django.conf.urls import patterns, include, url
from images.views import ImagesView
from sandboxes.views import SandboxListView

urlpatterns = patterns('',
    url(r'^images/$', ImagesView.as_view()),
    url(r'^sandboxes/$', SandboxListView.as_view()),
)
