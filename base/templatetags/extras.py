from django import template
import math

register = template.Library()


@register.filter
def get_int(value):
    return int(value)

@register.filter
def get_float(value):
    frac, whole = math.modf(value)
    if round(frac,2) == 0:
        frac = '00'
        return frac
    return int(round(frac,2)*100)


@register.simple_tag
def sub_values_get_int(price,deal):
    return int(price-deal)

@register.simple_tag
def sub_values_get_float(price,deal):
    frac, whole = math.modf(price-deal)
    if round(frac,2) == 0:
        frac = '00'
        return frac
    return int(round(frac,2)*100)


@register.filter
def get_pic_src(value):
    src = "{% static 'images/"+value+"'%}"
    print(src)
    return src


@register.simple_tag
def calc_profit(price,amzfee,ppfee,cost):
    profit = price*(1-amzfee/100)-ppfee-cost
    return profit