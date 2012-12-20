from django.conf.urls import patterns, url
from views import ActionItemList, ActionItemAdd, ActionItemUpdate

urlpatterns = patterns('',
    url(r'^$', ActionItemList.as_view(), name='actionitems_list'),
    url(r'add/$', ActionItemAdd.as_view(), name='actionitems_add'),
    url(r'(?P<pk>[\d]+)/$', ActionItemUpdate.as_view(), name='actionitems_update'),
    url(r'(?P<pk>[\d]+)/(?P<sync>sync)/$', ActionItemUpdate.as_view(), name='actionitems_sync'),
)
