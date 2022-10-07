
from email import message
from email.headerregistry import Address
from ftplib import FTP
from io import open_code
from itertools import product
from operator import mod
from pyexpat import model
from sys import modules
from turtle import title
from django.db import models
from datetime import datetime, date,time
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#model for for product videos
class Myvideo(models.Model):
    caption = models.CharField(max_length=250)
    video = models.FileField(upload_to="video/")

    def __str__(self):
        return self.caption

#Home page banner model 
class Banner(models.Model):
   
    image = models.ImageField(upload_to = "banner_images/")

    def __str__(self):
        return str(self.id)

#category model for products category display
CATEGORY_CHOICES = (
    ('Deal_of_the_day' , 'Deal_of_the_day'),
    ('Country_chicken' , 'Country_Chicken'),
    ('Poultry_chicken' , 'Poultry_chicken'),
    ('Mutton' , 'Mutton'),
    ('Fish_seafood ' , 'Fish_seafood'),
    ('Prawns' , 'Prawns'),
    ('Cold_cuts' , 'Cold_cuts'),
    ('Ready_to_cook' , 'Ready_to_cook')
    

)

class Category(models.Model):
    title = models.CharField(choices= CATEGORY_CHOICES , max_length=100 )
    image = models.ImageField(upload_to = "category_images/")

    def __str__(self):
        return str(self.title)


STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On the way' , 'On the way'),
    ('Delivered' , 'Delivered'),
    ('Canceled' , 'Canceled')
)

#product models
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    quantity = models.CharField(max_length=200, blank=False)
    pieces = models.CharField(max_length=100 , null=True, blank=True)
    product_image = models.ImageField(upload_to = 'producting/')
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()



#---------------------art-----------------

class Cart(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.user.username

    @property 
    def grandtotal(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.subtotal for item in cartitems])
        return total
    
    @property 
    def cartquantity(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

   
#cart Items
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , null=True)
    quantity = models.IntegerField(default=0 , null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title
    
    @property
    def subtotal(self):
        total =  self.product.discounted_price * self.quantity
        return total


ADDRESS_TYPE= (
    ('Home' , 'Home'),
    ('Work' , 'Work'),
    ('Others' , 'Others')

)


class UserProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField(max_length=250)
    mobile_number = PhoneNumberField()
    locality = models.CharField(max_length = 300, null=False)
    address = models.TextField(null=False)
    address_type = models.CharField(max_length=25 , choices=ADDRESS_TYPE, default= 'Home', null=True)
    city = models.CharField(max_length = 100)
    pincode = models.IntegerField(null=False)
    landmark = models.CharField(max_length=500)
    state = models.CharField(max_length = 100)
  

    def __str__(self):
        return str(self.user.username)



ORDER_STATUS = (
    ('pending' , 'pending'),
    ('on process' , 'on process'),
    ('out for delivery' , 'out for delivery'),
    ('delivered' , 'delivered'),
    ('cancelled' , 'cancelled')

)

PAYMENT_STATUS = (
    ('1' , 'success'),
    ('2' , 'failure'),
    ('3' , 'pending')

)


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    userprofile = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=200 , null=True)
    order_id = models.CharField(max_length=200, null=True)
    payment_id = models.CharField(max_length=250 , null=True)
    address = models.CharField(max_length=255, null=True)
    order_date = models.DateField(auto_now_add=False , auto_now=False, null=True)
    order_time = models.TimeField(auto_now_add=False , auto_now=False, null=True) 
    payment_status = models.CharField(max_length=50, choices = PAYMENT_STATUS , null=True)
    order_status = models.CharField(max_length=50, choices = ORDER_STATUS , default='3')

    def __str__(self):
        return '{} - {}'.format(self.id , self.order_id)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{}'.format(self.order.order_id)



#Wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return str(self.id)

  