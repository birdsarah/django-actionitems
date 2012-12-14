from django.conf.urls import patterns, include, url
from views import ActionItemList, ActionItemCreate, ActionItemUpdate, ActionItemSync

urlpatterns = patterns('',
    url(r'^$', ActionItemList.as_view(), name='actionitems_list'),
    url(r'add/$', ActionItemCreate.as_view(), name='actionitems_add'),
    url(r'(?P<pk>[\d]+)/$', ActionItemUpdate.as_view(), name='actionitems_edit'),
    url(r'(?P<pk>[\d]+)/sync/$', ActionItemSync.as_view(), name='actionitems_sync'),
)
