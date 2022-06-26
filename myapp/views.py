from http.client import HTTPResponse
from itertools import product
import json
from turtle import title
from unicodedata import category
from urllib import request
from django.shortcuts import render
from .models import *
from django.views import *
from .forms import UserRegistration
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def homePage(request):
    total_items = 0
    video = Myvideo.objects.all()
    banner = Banner.objects.all()
    category = Category.objects.all()
    dealOfTheDay = Product.objects.filter(category = 'Deal_of_the_day')
    #for time being , the below query need to change. it should be dealof the day
    fish = Product.objects.filter(category = 'Country_chicken')

    if request.user.is_authenticated:
        total_items = len(Cart.objects.filter(user = request.user))

    return render( request , 'myapp/home.html' , 
    {'video' : video , 
    'banner': banner , 
    'category' : category , 
    'DOTD' : dealOfTheDay ,
    'fish' : fish, 
    'total_items' : total_items,
    'active' : 'border-bottom border-danger border-2'})

 
def todaySale(request):
    todaySale = Product.objects.filter(category='Deal_of_the_day')
    todayDeal = Product.objects.filter(category = 'Deal_of_the_day')
    return render(request , 'myapp/todaysale.html' , {'todaydeal' : todayDeal})


def countryChickenProducts(request):
    countryChicken = Product.objects.filter(category = 'Country_chicken')
    return render(request , 'myapp/countrychicken.html' , {'countrychicken': countryChicken})




def poultryChickenProducts(request):
    poultryChicken = Product.objects.filter(category = 'Poultry_chicken')
    return render(request , 'myapp/countrychicken.html' , {'poultrychicken': poultryChicken })



def muttonProducts(request):

    mutton = Product.objects.filter(category = 'Mutton')
    return render(request , 'myapp/mutton.html' , {'mutton' : mutton})



def seafoodProducts(request):

    seaFood =Product.objects.filter(category = 'Fish_seafood')
    return render(request , 'myapp/seafood.html' , {'seafood' : seaFood})



def prawnsProducts(request):

    prawnsProducts = Product.objects.filter(category = 'Prawns')
    return render(request , 'myapp/prawns.html' , {'prawns' : prawnsProducts})


def readyToCookProducts(request):
    readytocook = Product.objects.filter(category = 'Ready_to_cook')
    return render(request , 'myapp/readytocookmeat.html' , {})



def coldCutProdcuts(request):
    coldcut = Product.objects.filter(category = 'Cold_cuts')
    return render(request , 'myapp/coldcut.html' , {'coldcut' : coldcut})


#single product details view

class ProductDetails(View):
    def get(self, request , pk):
        product = Product.objects.get(pk=pk)
        related_product = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
        return render(request , 'myapp/productdetails.html' , {'product':product , 'related_product' : related_product})


# Add to cart function View

def addToCart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = product_id)
    cart, created = Cart.objects.get_or_create(user=customer)
    cartitems, created = CartItems.objects.get_or_create(product=product, cart=cart)
    if action == 'add':
        cartitems.quantity += 1
    cartitems.save()




    return JsonResponse("its working" , safe=False)







'''
def addToCart(request):
    usr = request.user
    product_id = request.GET.get('product-id')
    product = Product.objects.get(id=product_id)
    savecart = Cart(user = usr , product = product)
    savecart.save()

    return redirect('/cart/')
'''


#Display cart page
def cartPage(request):
    if request.user.is_authenticated:
        user = request.user
        total_tems = 0
        total_amount = 0.0
        grand_amount = 0.0
        cart = Cart.objects.filter(user=user)
        cart_items = [p for p in Cart.objects.all() if p.user==user]
        if user.is_authenticated:
            total_items = len(Cart.objects.filter(user=user))

        if (cart_items):
            for c in cart_items:
                temporaryAmount = (c.product_qty * c.product.discounted_price)
                total_amount += temporaryAmount
                grand_amount = total_amount

            return render( request , 'myapp/showcart.html',{
                'cart' : cart,
                'total_amount' : total_amount,
                'grand_total' : grand_amount,
                'total_items' : total_items
                })
        else:
            return render(request , 'myapp/empty.html')




class SignUp(View):

    def get(sself, request):
        form = UserRegistration()
        return render (request , 'myapp/signup.html' , {'form' : form})

    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            messages.success(request , 'Congratulations!! you have registerted successfully. Please login')
            form.save()
            form = UserRegistration()

        return render (request , 'myapp/signup.html' , {'form' : form})









def checkoutCart(request):

    return render(request , 'myapp/checkout.html' , {})




def photoGallery(request):

    return render(request , 'myapp/gallery.html' , {})




def paymentPage(request):

    return render(request , 'myapp/payment.html' , {})


# search view

def searchProduct(request):
    if request.method == "GET":

        query = request.GET.get('q')

        if query:
            data = Product.objects.filter(title__icontains=query).order_by('-id')

            return render(request, 'myapp/search.html' , {'data' : data})

        else:
            return render(request, 'myapp/search.html' , {'data' : 'No products found'})



# add to wishlist Logic

def addToWishlist(request):
    prod_id = request.GET['product']
    product = Product.objects.get(id=prod_id)
    data = {}
    check_wishlish = Wishlist.objects.filter(product=product , user = request.user).count()
    if check_wishlish > 0:
        data = {
            'status' : 'Already in wishlist'
        }
    else:
        wishlist = Wishlist.objects.create(product= product , user=request.user)
        data = {

            'status' : 'Added to wishlist'
        }


    return JsonResponse(data)

#add to wish display
def myWishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user).order_by('-id')
    return render(request , 'myapp/wishlist.html' , {'wishlist': wishlist})