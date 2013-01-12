import pytest
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

    def test_1_model(self):
        assert ActionItemCreateView.model == ActionItem

    def test_2_template(self):
        assert ActionItemCreateView.template_name == 'actionitems/create.html'

    def test_3_formclass(self):
        assert ActionItemCreateView.form_class == ActionItemCreateForm

    # NB rf is the pytest.fixture for RequestFactory that comes with pytest-django    
    def test_getorigin_1_originnone_when_not_set(self, rf):
        actionitem_createview = ActionItemCreateView()
        origin = actionitem_createview.get_origin(actionitem_createview, rf)
        assert origin is None

    @pytest.mark.run_with_origin
    def test_getorigin_2_return_origin(self,rf):
        actionitem_createview = ActionItemCreateView()
        actionitem_createview.origin = 'notNone'
        origin = actionitem_createview.get_origin(actionitem_createview, rf)
        assert origin is 'notNone'

    @pytest.mark.run_with_origin
    def test_getorigin_3_raiseserror_when_origin_none(self, rf):
        actionitem_createview = ActionItemCreateView()
        with pytest.raises(ImproperlyConfigured):
            origin = actionitem_createview.get_origin(actionitem_createview, rf)

    @pytest.mark.run_with_origin
    def test_getinitial_1_sets_initial_origin(self, rf):
        get_request = rf.get('/')
        # get_initial is called during a get request on a CreateView form (via the FormMixin & ProcessFormMixin)
        response = ActionItemCreateViewWithDummyOrigin.as_view()(get_request)  
        assert response.context_data['form'].initial['origin'] == 'dummy origin'

    @pytest.mark.run_with_origin
    def test_getinitial_2_origin_not_set_on_post(self, rf):
        post_request = rf.post('/')
        response = ActionItemCreateViewWithDummyOrigin.as_view()(post_request) 
        print response.context_data['form'].initial 
        assert response.context_data['form'].initial == {}


# This is necessary for testing the with_origin branch. If using django-actionitems with ORIGIN_MODEL, the 
# implementer is expected to subclass ActionItemCreateView and provide the get_origin method themselves
class ActionItemCreateViewWithDummyOrigin(ActionItemCreateView):
    def get_origin(self, request, *args, **kwargs):
        return 'dummy origin'

class TestActionItemUpdateView:

    def test_1_model(self):
        assert ActionItemUpdateView.model == ActionItem

    def test_2_template(self):
        assert ActionItemUpdateView.template_name == 'actionitems/update.html'

    def test_3_formclass(self):
        assert ActionItemUpdateView.form_class == ActionItemUpdateForm

    def test_get_success_url(self):
        actionitemupdateview = ActionItemUpdateView()
        actionitemupdateview.kwargs = {'pk' : 1}
        url = actionitemupdateview.get_success_url()
        assert url._proxy____args[0] == 'actionitems_update'

    @pytest.mark.django_db # TODO How to do this without having to hit the database?
    def test_get_withsync(self, rf):
        actionitem = ActionItem.objects.create(description='dummy description')
        get_request = rf.get('/')
        actionitemupdateview = ActionItemUpdateView()
        actionitemupdateview.kwargs = {'pk' : actionitem.pk, 'sync': 'sync'}
        actionitemupdateview.request = get_request
        response = actionitemupdateview.get(get_request)
        # This is perhaps not the best way of confirming that the sync method was called, but its a start
        assert response.context_data['actionitem'].description == actionitem.description + ' sync'
