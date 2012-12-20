from models import ActionItem
from django.forms import ModelForm
from django.http import HttpRequest


class ActionItemAddForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActionItemAddForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs["class"] = 'actionitems-date-widget'

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
