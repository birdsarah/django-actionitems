from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ImproperlyConfigured
from datetime import date

from models import ActionItem
from forms import ActionItemCreateForm, ActionItemUpdateForm
from sync import sync
from settings import USE_ORIGIN_MODEL


class ActionItemListView(ListView):
    model = ActionItem
    template_name = 'actionitems/list.html'
    context_object_name = 'actionitems'


class ActionItemCreateView(CreateView):
    model = ActionItem
    template_name = 'actionitems/create.html'
    form_class = ActionItemCreateForm
    success_url = reverse_lazy('actionitems_list')

    origin = None

    def get_initial(self):
        initial = super(ActionItemCreateView, self).get_initial().copy()
        if self.request.method != 'POST':
            initial['origin'] = self.get_origin(self.request)
        return initial

    def get_origin(self, request, *args, **kwargs):
        # Expect an overriding method get_origin method to set origin
        if USE_ORIGIN_MODEL and self.origin is None:
            raise ImproperlyConfigured(u"Please write a get_origin method that returns the origin id")
        return self.origin


class ActionItemUpdateView(UpdateView):
    model = ActionItem
    template_name = 'actionitems/update.html'
    form_class = ActionItemUpdateForm

    def get_success_url(self):
        return reverse_lazy('actionitems_update', kwargs=self.kwargs)

    # Extra handling for when Sync is used in future
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('sync', None) == 'sync':
            sync(ActionItem.objects.get(pk=self.kwargs.get('pk')))
        return super(ActionItemUpdateView, self).get(request, *args, **kwargs)
