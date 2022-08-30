
from itertools import product
import json
from multiprocessing import context
from telnetlib import STATUS
from threading import local
from tkinter import E
import urllib.request 
from turtle import title
from typing import List
from unicodedata import category
from urllib import request
from django.shortcuts import render

from .models import *
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect , HttpResponse
from .forms import UserRegistration , LoginForm ,  UserProfileForm

import random

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
        customer = request.user
        cart, created = Cart.objects.get_or_create(user=customer)
        cartitems = cart.cartitem_set.all()
    else:
        cart = []
        cartitems = []
        cart = {'cartquantity': 0}


    return render( request , 'myapp/home.html' , 
    {'video' : video , 
    'banner': banner , 
    'category' : category , 
    'DOTD' : dealOfTheDay ,
    'fish' : fish, 
    'cart' : cart,
    'cartitems' : cartitems,
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

        if request.user.is_authenticated:
            customer = request.user
            cart, created = Cart.objects.get_or_create(user=customer)
            cartitems = cart.cartitem_set.all()
        else:
            cart = []
            cartitems = []
            cart = {'cartquantity': 0}

        return render(request , 'myapp/productdetails.html' , {'product':product , 'related_product' : related_product , 'cart' :cart , 'cartitems':cartitems})


# Add to cart function View
def addToCart(request):
    data = json.loads(request.body)
    productId = data['product_id']
    action = data['action']
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(id = productId)
        cart, created = Cart.objects.get_or_create(user=user)
        cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)
        

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()

        msg = {

            'cartQuantity' : cart.cartquantity


        }
    return JsonResponse( msg ,  safe=False)

# cart items display
def cartItems(request):
    if request.user.is_authenticated:
        user = request.user
        cart, create = Cart.objects.get_or_create(user=user)
        cartitems = cart.cartitem_set.all()

    else:
        cart = []
        cartitems = []
    context = {'cart' : cart , 'cartitems' : cartitems}

    return render(request, 'myapp/cartpage.html' , context)




# update cart quantity

# minus cart item
def minusCartItem(request):
    if request.method == "GET":
        prod_id = request.GET['product_id']
        print(prod_id)
        cart = CartItem.objects.get(Q(product= prod_id))
        cart.quantity -= 1
        cart.save()

    return JsonResponse('Successfully cart item decresed' , safe=False)


#plus cart item
def plusCartItem(request):
    if request.method == "GET":
        prod_id = request.GET['product_id']
        print(prod_id)
        cart = CartItem.objects.get(Q(product= prod_id))
        print(cart)
        cart.quantity += 1
        cart.save()

    return JsonResponse('Successfully cart item decresed' , safe=False)







'''
def updateCartQuantity(request):
    data = json.loads(request.body)
    print(data)
    product_id = data['product_id']
    itemValue = data['itemValue']
    print(product_id , itemValue)
    user = request.user
    product = Product.objects.get(id = product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cartitems, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cartitems.quantity = itemValue
    cartitems.save()
    msg = {
        'subtotal':cartitems.subtotal,
        'grandtotal': cart.grandtotal,
        'quantity': cart.cartquantity
    }

    return JsonResponse(msg , safe=False)

'''






'''
def deleteCartItem(request):
   


    return JsonResponse({'status': 'Deleted successfully'})

#delete cart item
'''


'''
def addToCart(request):
    usr = request.user
    product_id = request.GET.get('product-id')
    product = Product.objects.get(id=product_id)
    savecart = Cart(user = usr , product = product)
    savecart.save()

    return redirect('/cart/')



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


'''


#---------------sign up view--------------------
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




#----------------------checkout page-----------------------
def checkoutCart(request):
    cart = Cart.objects.get(user=request.user)
    rawcart =  cart.cartitem_set.all()
    order = Order.objects.filter(user = request.user)
    profile = UserProfile.objects.filter(user=request.user)
    form = UserProfileForm()
   
    context = {'order' : order,
                'address' : profile,
                'form' : form}
    return render(request , 'myapp/checkout.html' , context)




# ----------------userprofile  address-----------------


'''
def userProfileAddress(request):
    form = UserProfileForm()

    return render(request , 'myapp/useraddress.html', {'form' : form})

'''

def userProfileAddress(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        mobile_number = data['mobile_number']
        address = data['address']
        locality = data['locality']
        city = data['city']
        landmark = data['landmark']
        state = data['state']
        pincode = data['pincode']
        address_type = data['address_type']
        user_data = UserProfile(user=user , first_name = first_name, last_name = last_name, email=email, mobile_number=mobile_number, address=address, locality=locality,
        city=city , landmark=landmark , state=state, pincode = pincode, address_type = address_type)
        user_data.save()
        user_data_value = UserProfile.objects.values()
        user_list = list(user_data_value)
        
        return JsonResponse({'status': 'address added' , 'user_list':user_list} , status=200 , safe=False)
    
    return JsonResponse("Invalid request" , safe=False )

  
   

''''
def editUserAddress(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)

        userProfile = UserProfile.objects.get(pk=id)
        print(userProfile)
        userProfileData = f'{{"id" : {userProfile.id}, "first_name" : {userProfile.first_name} , "last_name" : {userProfile.last_name}, "email" : {userProfile.email}, "mobile_number": {userProfile.mobile_number}, "address" : {userProfile.address}, "locality" : {userProfile.locality}, "city": {userProfile.city}, "landmark" : {userProfile.landmark}, "state" : {userProfile.state} , "pincode": {userProfile.pincode}, "addres_type": {userProfile.address_type} }}'
     
        return JsonResponse(userProfileData , safe=False)



'''
#----------------------------------edit user address view---------------
class EditAddress(View):
    def get(self, request , id):
        pi = UserProfile.objects.get(pk = id)
        form = UserProfileForm(instance=pi)
        return render(request, 'myapp/editaddress.html' ,{'form' : form})
    def post(self, request, id):
        pi = UserProfile.objects.get(pk=id)
        form = UserProfileForm(request.POST , instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/checkout-cart/')
        return render(request, 'myapp/editaddress.html' , {'form' : form})
        

def updateAddress(request, id=0):
    '''    if request.method=="POST":
        pi = UserProfile.objects.get(pk=id)
        form = UserProfileForm(request.POSt , instance=pi)
        if form.is_valid():
            form.save()
        return redirect('/checkout-cart/')
        #return render(request, 'myapp/editaddress.html' , {'form' : form})

    else:
        pi = UserProfile.objects.get(pk=id)
        form = UserProfileForm( instance=pi)
        return render(request, 'myapp/editaddress.html' , {'form' : form})

    '''
    if request.method == "GET":
        if id == 0:
            form = UserProfileForm()
        else:
            userAddress = UserProfile.objects.get(pk=id)
            form = UserProfileForm(instance=userAddress)
        return render(request, 'myapp/editaddress.html' , {'form' : form})

    else:
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/checkout-cart/')





#--------------------------Order details view----------

def placeOrder(request):
    if request.method == 'POST':
        user_profile = UserProfile()
        neworder = Order()
        neworder.user = request.user
        neworder.order_date = request.POST.get('order_date')
        neworder.order_time = request.POST.get('order_time')
        #neworder.address_type = request.POST.get('address_type')
        #neworder.userprofile = request.POST.get('custid')
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.address = request.POST.get('customerid')
        total_cart_price = 0
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        for item in cart_items:
            total_cart_price = (int(item.product.discounted_price) * item.quantity)
        neworder.total_price = total_cart_price

        orderId = 'freshmeatz' + str(random.randint(111111,999999))
        while Order.objects.filter(order_id = orderId):
            orderId = 'OD' + str(random.randint(111111,999999))
        
        neworder.order_id = orderId
        neworder.save()
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            OrderItem.objects.create(
                order =neworder,
                product = item.product,
                price = item.product.discounted_price,
                quantity = item.quantity


            )

        Cart.objects.filter(user=request.user).delete()

    return redirect('orderpayment/')


#------------------cash on deliveryy option view
def order_done(request):

    return render(request, 'myapp/orderdone.html')




def photoGallery(request):

    return render(request , 'myapp/gallery.html' , {})




def paymentPage(request):

    return render(request , 'myapp/payment.html' , {})


#-----------------------search view----------------------------

def searchProduct(request):
    if request.method == "GET":
        query = request.GET.get('q')

        if query:
            data = Product.objects.filter(title__icontains=query).order_by('-id')

            return render(request, 'myapp/search.html' , {'data' : data})

        else:
            return render(request, 'myapp/search.html' , {'data' : 'No products found'})



# ----------------------dd to wishlist Logic--------------------

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
    total_wishlist= len(Wishlist.objects.filter(user = request.user))
    return render(request , 'myapp/wishlist.html' , {'wishlist': wishlist , 'w' : total_wishlist})

# delete wishlist item
def deleteWishlist(request):
    if request.user.is_authenticated:
        prod_id = int(request.GET.get('product_id'))
        if(Wishlist.objects.filter(user=request.user, product_id = prod_id)):
            wishlistitem = Wishlist.objects.get(product_id=prod_id)
            wishlistitem.delete()

            return JsonResponse({'status' : 'Item has been removed'})


        else:
            return JsonResponse({'status' : "Item nit found in wishlist"})

    else:
        return JsonResponse({'status' : 'Login required to remove'})

    return redirect("/")



# customer addres view

def address(request):
    return render(request , 'myapp/addres.html')