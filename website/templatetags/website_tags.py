from django import template

register = template.Library()

@register.filter(name='split_dash')
def split_dash(value):
    return str(value).split('-')[0].strip().capitalize()

@register.filter(name='upper_letter')
def upper_letter(value):
    return str(value).upper()