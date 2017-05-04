__author__ = 'asilvio'
from django.conf.urls import patterns, url

urlpatterns = patterns('Seg.apps.main.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^contact/$', 'contact_view', name='contact'),
    url(r'^specials/$', 'specials_view', name='dishes'),

)
