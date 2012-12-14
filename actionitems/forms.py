from models import ActionItem
from django.forms import ModelForm
from django.http import HttpRequest


class ActionItemCreateForm(ModelForm):
    class Meta:
        model = ActionItem
        exclude = ('completed_on', 'created_on', 'updated_on')


class ActionItemUpdateForm(ModelForm):
    class Meta:
        model = ActionItem
        exclude = ('completed_on', 'created_on', 'updated_on', 'manager')
