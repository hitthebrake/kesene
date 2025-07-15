from django import template

register = template.Library()

@register.filter
def get_item(lst, key):
    for dictionary in lst:
        if dictionary['type'] == key:
            return dictionary['value']
    return ""