from re import search
from datetime import date, datetime

from django.utils.html import strip_tags
from django.db import models

from actionitems.settings import *


class ActionItem(models.Model):
    description = models.TextField(null=True, blank=True)
    responsible = models.CharField(max_length=100)
    deadline = models.DateField(null=True, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(null=True, blank=True)
    manager = models.CharField(max_length=10, choices=MANAGER_LIST, default=MANAGER_LIST[0][0])

    # USE_ORIGIN_MODEL and ORIGIN_MODEL come from actionitems.settings
    if USE_ORIGIN_MODEL:
        origin = models.ForeignKey(ORIGIN_MODEL, null=True, blank=True)

    def is_done(self):
        if self.completed_on:
            if date.today() >= self.completed_on:
                return True
        return False

    def title(self):
        description = strip_tags(self.description)
        match = search("\.|\\r|\\n", description)
        title_length = 140
        if match:
            start = match.start()
            if start < title_length:
                position = start
        return description[:title_length]
