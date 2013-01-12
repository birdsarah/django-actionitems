from models import ActionItem
from django.forms import ModelForm
from django.http import HttpRequest
from django.forms.widgets import HiddenInput

from settings import USE_ORIGIN_MODEL

class ActionItemCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActionItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs["class"] = 'actionitems-date-widget'
        # We have to give origin so that the origin field can be posted and a new item created, so mark as hidden
        if USE_ORIGIN_MODEL:        
            self.fields['origin'].widget = HiddenInput()

    class Meta:
        model = ActionItem
        exclude = ('completed_on', 'created_on', 'updated_on')


class ActionItemUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActionItemUpdateForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs["class"] = 'actionitems-date-widget'

    class Meta:
        model = ActionItem
        exclude = ('completed_on', 'created_on', 'updated_on', 'origin', 'manager')
