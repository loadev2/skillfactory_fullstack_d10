from django import template
from common.models import Car

register = template.Library()

@register.filter
def trans_name(value):
    value_arr=[x[1] for x in Car.TRANS_TYPE]
    return value_arr[value-1]