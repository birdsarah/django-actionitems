from django.conf import settings
from django.db.models import get_model

USE_ORIGIN_MODEL = getattr(settings, 'ACTIONITEMS_ORIGIN_MODEL', False)

if USE_ORIGIN_MODEL:
    model_string = getattr(settings, 'ACTIONITEMS_ORIGIN_MODEL')
    ORIGIN_MODEL = get_model(*model_string.split('.'))

default_manager_list = (('internal', 'Internal'),)
MANAGER_LIST = getattr(settings, 'ACTIONITEMS_MANAGER_LIST', default_manager_list)
