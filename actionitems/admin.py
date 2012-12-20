from models import ActionItem
from django.contrib import admin

class ActionItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'responsible', 'deadline', 'done')

admin.site.register(ActionItem, ActionItemAdmin)
