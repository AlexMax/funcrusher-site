from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'servers.views.passwords'),
    url(r'^request/(?P<server_id>\d+)/$', 'servers.views.password_request'),
)
