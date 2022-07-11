from itertools import product
from turtle import title
from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Myvideo)

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id' ,  'image']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'image']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'selling_price' , 'discounted_price' , 'category' , 'product_image' , 'date_added']

@admin.register(Wishlist)
class WhishlistModelAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'added_at']
   

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user' , 'created_at']

@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['cart' , 'product' , 'quantity' , 'date_added']