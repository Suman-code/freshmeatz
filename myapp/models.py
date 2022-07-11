from itertools import product
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User

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
        return str(self.category)


STATUS_CHOICES = (
    ('Accepted' , 'Accepted'),
    ('Packed' , 'Packed'),
    ('On the way' , 'On the way'),
    ('Delivered' , 'Delivered'),
    ('Canceled' , 'Canceled')
)

#product models
class Product(models.Model):
    category = models.CharField(choices = CATEGORY_CHOICES ,  max_length = 100)
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
# cart

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



class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=242)
    locality = models.CharField(max_length = 300, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length = 100)
    pincode = models.IntegerField(null=False)
    landmark = models.CharField(max_length=500)
    state = models.CharField(max_length = 100)
  

    def __str__(self):
        return str(self.id)


'''
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    order_Date = models.DateTimeField(auto_now_add = True)
    updated_Date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES , default='pending')

    def __str__(self):
        return str(self.id)


'''
#Wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return str(self.id)

  