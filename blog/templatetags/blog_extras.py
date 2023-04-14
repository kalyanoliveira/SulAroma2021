# Lines from Django documentation's website 
from django import template
register = template.Library()

# Registering of template tag into template library via python decorator
@register.filter
# Template tag that replaces a specified piece of string with a space character
def nbsp(value, arg):
    return value.replace(arg, ' ')