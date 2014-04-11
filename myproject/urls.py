from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikimedia_identities.views.home', name='home'),
    url(r'^editor/', include('editor.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
