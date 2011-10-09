from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from profiles.forms import UserRegistrationForm
from registration.views import register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/register/$', register, {
        'backend': 'registration.backends.default.DefaultBackend',
        'form_class': UserRegistrationForm,
    }, name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
