import pytest
from django.test.client import RequestFactory
from django.core.exceptions import ImproperlyConfigured

from actionitems.views import ActionItemListView, ActionItemCreateView, ActionItemUpdateView
from actionitems.models import ActionItem
from actionitems.forms import ActionItemCreateForm, ActionItemUpdateForm
import actionitems.settings as actionitems_settings


class TestActionItemListView:
    def test_actionitemlist_1_model(self):
        assert ActionItemListView.model == ActionItem

    def test_actionitemlist_2_template(self):
        assert ActionItemListView.template_name == 'actionitems/list.html'

    def test_actionitemlist_3_contextobject(self):
        assert ActionItemListView.context_object_name == 'actionitems'

class TestActionItemCreateView:
    def test_actionitemcreate_1_model(self):
        assert ActionItemCreateView.model == ActionItem

    def test_actionitemcreate_2_template(self):
        assert ActionItemCreateView.template_name == 'actionitems/create.html'

    def test_actionitemcreate_3_formclass(self):
        assert ActionItemCreateView.form_class == ActionItemCreateForm

    def test_actionitemcreate_getorigin_1_originnone_when_not_set(self):
        request = RequestFactory()
        actionitem_createview = ActionItemCreateView()
        origin = actionitem_createview.get_origin(actionitem_createview, request)
        assert origin is None

    @pytest.mark.run_with_origin 
    def test_actionitemcreate_getorigin_2_return_origin(self):
        request = RequestFactory()
        actionitem_createview = ActionItemCreateView()
        actionitem_createview.origin = 'notNone'
        origin = actionitem_createview.get_origin(actionitem_createview, request)
        assert origin is 'notNone'

    @pytest.mark.run_with_origin
    def test_actionitemcreate_getorigin_3_raiseserror_when_origin_none(self):
        request = RequestFactory()
        actionitem_createview = ActionItemCreateView()
        with pytest.raises(ImproperlyConfigured):
            origin = actionitem_createview.get_origin(actionitem_createview, request)

    
