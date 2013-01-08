import os
from datetime import datetime, timedelta
from django.utils.timezone import utc
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

from actionitems.models import ActionItem


class TestHandleDone:
    def test_handle_done_1_with_done_null(self):
        # With actionitem.done not set, completed on should be empty
        actionitem = ActionItem()
        actionitem = actionitem.handle_done(actionitem)
        assert actionitem.completed_on is None

    def test_handle_done_2_with_done_null_when_completed_on_has_initial_value(self):
        # With actionitem.done not set, completed on should be forced empty
        actionitem = ActionItem()
        actionitem.completed_on = datetime.now()
        actionitem = actionitem.handle_done(actionitem)
        assert actionitem.completed_on is None

    def test_handle_done_3_with_done_set_when_completed_on_has_not_been_set(self):
        # With actionitem.done set, completed on should be set
        actionitem = ActionItem()
        actionitem.done = True
        actionitem = actionitem.handle_done(actionitem)
        delta = actionitem.completed_on - datetime.utcnow().replace(tzinfo=utc)
        assert abs(delta) <= timedelta(milliseconds=10), 'Times are not almost equal'

    def test_handle_done_4_with_done_set_false_removes_completed_on(self):
        # Completed on should be removed if done is false
        actionitem = ActionItem()
        completed_on = datetime.now() + timedelta(days=-22)
        actionitem.completed_on = completed_on
        actionitem = actionitem.handle_done(actionitem)
        assert actionitem.completed_on is None

    def test_handle_done_5_with_done_true_and_completed_on_in_past_that_completed_on_remains(self):
        # Completed on shouldn't change if nothing has changed
        actionitem = ActionItem()
        completed_on = datetime.now() + timedelta(days=-32)
        actionitem.completed_on = completed_on
        actionitem.done = True
        actionitem = actionitem.handle_done(actionitem)
        assert actionitem.completed_on == completed_on


