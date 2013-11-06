from django.conf.urls import patterns, include, url
from django.contrib import admin

from images.views import ImagesView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opendevelop.views.home', name='home'),
    # url(r'^opendevelop/', include('opendevelop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/images/', ImagesView.as_view()),
)
