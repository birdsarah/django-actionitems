import pytest
from django.conf import settings
import actionitems.settings as actionitems_settings
from actionitems.models import ActionItem

def _set_settings(name, value):
    settings.__setattr__(name, value)
    reload(actionitems_settings)

class TestOriginModel():
    def test_origin_model_1_when_none_set_check_use(self):
        _set_settings('','')
        assert actionitems_settings.USE_ORIGIN_MODEL is False

    def test_origin_model_2_when_none_set_check_origin_model(self):
        _set_settings('','')
        with pytest.raises(AttributeError):
            actionitems_settings.ORIGIN_MODEL

    def test_origin_model_3_when_set_check_use(self):
        _set_settings('ACTIONITEMS_ORIGIN_MODEL','app.Model')
        assert actionitems_settings.USE_ORIGIN_MODEL is not False

    def test_origin_model_4_when_set_check_origin_model(self):
        _set_settings('ACTIONITEMS_ORIGIN_MODEL','actionitems.ActionItem')
        assert type(actionitems_settings.ORIGIN_MODEL) == type(ActionItem)


class TestManagerList():
    def test_manager_list_1_check_default(self):
        _set_settings('','')
        assert actionitems_settings.MANAGER_LIST == (('internal', 'Internal'),)
