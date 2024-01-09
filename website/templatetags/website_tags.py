from django import template
from website.models import Comment

register = template.Library()

@register.filter(name='split_dash')
def split_dash(value):
    return str(value).split('-')[0].strip().capitalize()

@register.filter(name='upper_letter')
def upper_letter(value):
    return str(value).upper()

@register.simple_tag(name='get_replies')
def get_replies(comment):
    reps = Comment.objects.filter(ref_id=comment.id)
    return reps