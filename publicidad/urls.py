from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'publicidad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ads/', include('ads.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
