from django.conf.urls import patterns, include, url
from home.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webshow.views.home', name='home'),
    # url(r'^webshow/', include('webshow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^login/$',login),
    url(r'^register/$',register),
    url(r'^draw/$',draw),
)
   
