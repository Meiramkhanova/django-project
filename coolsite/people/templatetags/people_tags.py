from django import template
from people.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()