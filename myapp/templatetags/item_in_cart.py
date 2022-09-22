from atexit import register
from ctypes.wintypes import PINT
from django import template
from .. models import Product
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(d, cartitems):

    print(d)



   

    


 
  

    