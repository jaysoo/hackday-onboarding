from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag('common/snippets/_field.html')
def display_field(field, *args, **kwargs):
	context = { 
		'field': field,
		'conf': settings.DISPLAY_FIELD_DEFAULTS
	}
	if 'required' in kwargs:
		context['required'] = True
	return context


@register.filter
def get_range(value, arg = 0):
	"""
	Filter - returns a list containing range made from given value
	Usage (in template):

		<ul>{% for i in 3|get_range %}
		  <li>{{ i }}. Do something</li>
		{% endfor %}</ul>

		Results with the HTML:
		<ul>
		  <li>0. Do something</li>
		  <li>1. Do something</li>
		  <li>2. Do something</li>
		</ul>
	"""
	try: 
		start = int(arg)
	except ValueError: 
		start = 0
		
	return range(start, value+1)

	
@register.filter
def keyvalue(dict, key):    
    return dict[key]


@register.filter
def dots_to_underscores(value):
	return value.replace('.', '_')