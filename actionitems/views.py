from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from datetime import date

from models import ActionItem
from forms import ActionItemCreateForm, ActionItemUpdateForm


class ActionItemList(ListView):
    model = ActionItem
    template_name = 'actionitems/list.html'
    context_object_name = 'actionitems'


class ActionItemCreate(CreateView):
    model = ActionItem
    template_name = 'actionitems/create.html'
    success_url = reverse_lazy('actionitems_list')
    form_class = ActionItemCreateForm

    def get(self, request, *args, **kwargs):
        self.origin = request.GET.get('actionitems_origin')
        print self.origin
        return super(ActionItemCreate, self).get(request, *args, **kwargs)

    def get_initial(self):
        initial = super(ActionItemCreate, self).get_initial().copy()
        if not self.request.POST:
            initial['origin'] = self.origin
        return initial


class ActionItemUpdate(UpdateView):
    model = ActionItem
    template_name = 'actionitems/edit.html'
    form_class = ActionItemUpdateForm

    def post(self, request, *args, **kwargs):
        actionitem = ActionItem.objects.get(pk=kwargs.get('pk'))
        self.handle_done(request, actionitem)
        return super(ActionItemUpdate, self).post(request, *args, **kwargs)

    def handle_done(self, request, actionitem):
        f = ActionItemUpdateForm(request.POST, instance=actionitem)
        actionitem = f.save(commit=False)
        if not actionitem.completed_on and 'done' in request.POST:
            actionitem.completed_on = date.today()
        if actionitem.completed_on and not 'done' in request.POST:
            actionitem.completed_on = None
        actionitem.save()


class ActionItemSync(UpdateView):

    def get(self, request, *args, **kwargs):
        instancepk = kwargs.get('pk')
        self.sync(ActionItem.objects.get(pk=instancepk))
        return redirect('actionitems_edit', pk=instancepk)

    def sync(self, actionitem):
        f = ActionItemUpdateForm(instance=actionitem)
        actionitem = f.save(commit=False)
        # TODO In the future this will pull in data from external managers
        actionitem.description += ' sync'
        actionitem.save()
