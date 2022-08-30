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


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user' , 'userprofile', 'address' , 'total_price' , 'order_id', 'payment_mode' ,'payment_id' ,'order_date', 'order_time',  'order_status']

@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['order' , 'product' , 'price' , 'quantity']

@admin.register(UserProfile)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user' ,'id' , 'first_name' , 'last_name' , 'city' , 'locality' , 'landmark' , 'pincode' , 'state']


