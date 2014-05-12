from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ads.views.index', name='ads-index'),
)
