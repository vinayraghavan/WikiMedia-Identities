from django.conf.urls import patterns, url

from editor import views

urlpatterns = patterns('',
	url(r'^registration/$', views.registration_page),
	url(r'^registration_successful/$', views.registration_successful),
	url(r'^login/$', views.login_page),
        url(r'^profile/(?P<username>[^/]+)$', views.user_profile),
	url(r'^loggedin/$', views.loggedin),
	url(r'^logging_out/$', views.logging_out),
	url(r'^invalid/$', views.invalid),
	url(r'^loggedout/$', views.loggedout),
	)
