django-actionitems
==================

To use django-actionitems, add <code>actionitems</code> to your INSTALLED_APPS in your project's settings.py

django-actionitems can store a reference to sommething that creates the actionitem. For example, an action item may be the result of a Meeting, Event, or Decision. django-actionitems calls this the origin. If you wish to link your actionitem to an origin, you can supply the model in your project's settings.py in the form appname.Model e.g.

```python
 ACTIONITEMS_ORIGIN_MODEL = 'publicweb.Decision'
``` 
If ACTIONITEMS_ORIGIN_MODEL is set, then django-actionitems expects an origin to be provided when adding a new actionitem. The easiest way to do this is to override the get_origin method ActionItemAdd in views.py.
The origin is the pk of the object. For example, if our origin is a "decision", we might set origin as follows: 
```python
from actionitems.views import ActionItemAdd


class MyCustomActionItemCreate(ActionItemAdd):

    def get_origin(self, request, *args, **kwargs):
            origin = kwargs.get('decisionpk')
            return origin
``` 
get_origin() is called by the get() method of ActionItemAdd, if you override get(), remember to supply an origin or manually call get_origin()
