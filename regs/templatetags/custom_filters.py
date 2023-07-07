from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr):
    return getattr(obj, attr)


@register.filter
def dict_items(value):
    if hasattr(value, 'items'):
        return value.items()
    return []

@register.filter
def startswithunderscore(value):
    return value.startswith('_')

@register.filter
def remove_underscore(value):
    return value.replace('_', ' ')
