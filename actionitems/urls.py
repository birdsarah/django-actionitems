from django.conf.urls import patterns, url
from views import ActionItemListView, ActionItemCreateView, ActionItemUpdateView

urlpatterns = patterns('',
    url(r'^$', ActionItemListView.as_view(), name='actionitems_list'),
    url(r'add/$', ActionItemCreateView.as_view(), name='actionitems_create'),
    url(r'(?P<pk>[\d]+)/$', ActionItemUpdateView.as_view(), name='actionitems_update'),
    url(r'(?P<pk>[\d]+)/(?P<sync>sync)/$', ActionItemUpdateView.as_view(), name='actionitems_sync'),
)
