import pytest
from django.conf import settings
import actionitems.settings as actionitems_settings
from actionitems.models import ActionItem


class TestOriginModel():
    def test_origin_model_1_when_none_set_check_use(self):
        reload(actionitems_settings)
        assert actionitems_settings.USE_ORIGIN_MODEL is False

    def test_origin_model_2_when_none_set_check_origin_model(self):
        reload(actionitems_settings)
        with pytest.raises(AttributeError):
            actionitems_settings.ORIGIN_MODEL

    def test_origin_model_3_when_set_check_use(self):
        settings.ACTIONITEMS_ORIGIN_MODEL = 'app.Model'
        reload(actionitems_settings)
        assert actionitems_settings.USE_ORIGIN_MODEL is not False

    def test_origin_model_4_when_set_check_origin_model(self):
        settings.ACTIONITEMS_ORIGIN_MODEL = 'actionitems.ActionItem'
        reload(actionitems_settings)
        assert type(actionitems_settings.ORIGIN_MODEL) == type(ActionItem)


class TestManagerList():
    def test_manager_list_1_check_default(self):
        reload(actionitems_settings)
        assert actionitems_settings.MANAGER_LIST == (('internal', 'Internal'),)
