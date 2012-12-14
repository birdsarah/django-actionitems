django-actionitems
==================

To use django-actionitems, add 'actionitems' to your INSTALLED_APPS in your project's settings.py

django-actionitems can store a reference to sommething that creates the actionitem. For example, an action item may be the result of a Meeting, Event, or Decision. django-actionitems calls this the origin. If you wish to link your actionitem to an origin, you can supply the model in your project's settings.py in the form appname.Model e.g.

 ACTIONITEMS_ORIGIN_MODEL = 'publicweb.Decision'
 
To include a link to add a decision in your template use:

<a href="{% url 'actionitems_add' %}?actionitems_origin={{ object.pk }}">Add Action Item</a> 

object should match the origin_model, if it doesn't the app will run, but the wrong origin instance will likely be selected. 

Some basic templates are provided as a convenience. You can insert them directly into your existing templates by using the {% include %} template tag. Choose from:
* actionitems/list.html
* actionitems/edit.html
* actionitems/create.html

For list.html to work correctly, you will need to supply actionitems in the view's context.
