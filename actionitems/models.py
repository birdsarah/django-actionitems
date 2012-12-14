from django.db import models
from datetime import date, datetime
from actionitems.settings import *

ACTIONITEMS_MANAGERS = (
    ('internal', 'Internal'),
    ('kanban', 'Kanban'))


class ActionItem(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    responsible = models.CharField(max_length=100)
    deadline = models.DateField(null=True, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(null=True, blank=True)
    manager = models.CharField(max_length=10, choices=ACTIONITEMS_MANAGERS, default='internal')

    # USE_ORIGIN_MODEL and ORIGIN_MODEL come from actionitems.settings
    if USE_ORIGIN_MODEL:
        origin = models.ForeignKey(ORIGIN_MODEL, null=True, blank=True)

    def is_done(self):
        if self.completed_on:
            if date.today() >= self.completed_on:
                return True
        return False

#class KanbanSetUp(models.Model):
#    api_key = models.CharField(max_length=100)

#class KanbanAction(models.Model):
#    action_item = models.ForeignKey(ActionItem)
#    kanban_id = models.IntegerField()
#    board = models.IntegerField()
#    synced_on = models.DateTimeField()
