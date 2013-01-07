django-actionitems
==================

To use django-actionitems, add <code>actionitems</code> to your INSTALLED_APPS in your project's settings.py

django-actionitems can store a reference to sommething that creates the actionitem. For example, an action item may be the result of a Meeting, Event, or Decision. django-actionitems calls this the origin. If you wish to link your actionitem to an origin, you can supply the model in your project's settings.py in the form appname.Model e.g.

```python
 ACTIONITEMS_ORIGIN_MODEL = 'publicweb.Decision'
``` 
