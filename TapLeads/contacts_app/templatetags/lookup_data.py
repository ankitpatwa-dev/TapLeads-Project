from django import template
register = template.Library()

@register.filter
def lookup_data(d, key):
    return d[key]
