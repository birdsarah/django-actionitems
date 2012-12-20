from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.core.exceptions import ImproperlyConfigured
from datetime import date

from models import ActionItem
from forms import ActionItemAddForm, ActionItemUpdateForm

from actionitems.settings import USE_ORIGIN_MODEL

class ActionItemList(ListView):
    model = ActionItem
    template_name = 'actionitems/list.html'
    context_object_name = 'actionitems'


class ActionItemAdd(CreateView):
    model = ActionItem
    template_name = 'actionitems/create.html'
    form_class = ActionItemAddForm
    success_url = reverse_lazy('actionitems_list')
    
    origin = None

    def get(self, request, *args, **kwargs):
        self.origin = self.get_origin()
        return super(ActionItemAdd, self).get(request, *args, **kwargs)

    def get_initial(self):
        initial = super(ActionItemAdd, self).get_initial().copy()
        if not self.request.POST:
            initial['origin'] = self.origin
        return initial

    def get_origin(self):
        # Expect an overriding method get_origin method to set origin
        if USE_ORIGIN_MODEL and self.origin == None:
            raise ImproperlyConfigured(u"Please write a get_origin method that returns the origin id")
        return self.origin
            

class ActionItemUpdate(UpdateView):
    model = ActionItem
    template_name = 'actionitems/update.html'
    form_class = ActionItemUpdateForm

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('sync', None) == 'sync':
            self.sync(ActionItem.objects.get(pk=self.kwargs.get('pk')))
        return super(ActionItemUpdate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return redirect('actionitems_update', pk=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        actionitem = ActionItem.objects.get(pk=kwargs.get('pk'))
        return super(ActionItemUpdate, self).post(request, *args, **kwargs)
        
    def sync(self, actionitem):
        f = ActionItemUpdateForm(instance=actionitem)
        actionitem = f.save(commit=False)
        # TODO In the future this will pull in data from external managers
        actionitem.description += ' sync'
        actionitem.save()
        return actionitem
