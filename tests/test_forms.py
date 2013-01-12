import pytest
from actionitems.forms import ActionItemCreateForm, ActionItemUpdateForm
from django.forms.widgets import HiddenInput

class TestActionItemCreateForm:

    def test_actionitemcreateform_deadline_widget_class(self):
        actionitemcreateform = ActionItemCreateForm()
        assert actionitemcreateform.fields['deadline'].widget.attrs["class"] == 'actionitems-date-widget'

    def test_actionitemcreateform_exclude_fields(self):
        actionitemcreateform = ActionItemCreateForm()
        assert actionitemcreateform.Meta.exclude == ('completed_on', 'created_on', 'updated_on') 

    @pytest.mark.run_with_origin
    def test_actionitemcreateform_origin_hidden_widget(self):
        actionitemcreateform = ActionItemCreateForm()
        assert type(actionitemcreateform.fields['origin'].widget) == HiddenInput

class TestActionItemUpdateForm:

    def test_actionitemupdateform_deadline_widget_class(self):
        actionitemupdateform = ActionItemUpdateForm()
        assert actionitemupdateform.fields['deadline'].widget.attrs["class"] == 'actionitems-date-widget'

    def test_actionitemupdateform_exclude_fields(self):
        actionitemupdateform = ActionItemUpdateForm()
        assert actionitemupdateform.Meta.exclude == ('completed_on', 'created_on', 'updated_on', 'origin', 'manager')
