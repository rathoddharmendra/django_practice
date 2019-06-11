from django import template

register = templare.Library()

def cutter(value,arg):
    """
    This is a customer filter to cut all values of "arg" from the string!
    """
    return value.replace(arg,'')

register.filter('cut_me', cutter)
