import math

from django import template

register = template.Library()

@register.filter(name="length")
def length(value):
    """calculates length """
    return len(value.tagged.all())*"*"



@register.filter(name="get4")
def get4(value):
    """calculates length """
    return int(math.ceil(len(value.tagged.all())/4))*"*"




@register.filter(name="divide")
def divide(value,arg):
    """calculates length """
    return int(value)//int(arg)



@register.filter(name="my_filter")
def my_filter(value,arg=0):
    """calculates length """
    print("value is ",value)
    print("args is",arg)
    arg=arg-1
    print(type(value))
    return value[4*arg:4*arg+4]


