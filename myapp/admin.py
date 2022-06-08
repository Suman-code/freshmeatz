from itertools import product
from turtle import title
from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Myvideo)

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'image']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'category' , 'image']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'selling_price' , 'discounted_price' , 'category' , 'product_image' , 'date_added']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'product_qty' , 'created_at']


   

