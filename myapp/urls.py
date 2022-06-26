from unicodedata import name
from django.urls import path 
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from . forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
path( '' , views.homePage , name='home'),
#Deal of the day url
path('todays-sale/' , views.todaySale , name="todaysale"),
#mutton prodcuts url
path('muttonitems/' ,  views.muttonProducts , name="mutton"),
#fish and seafood url
path('seafooditems/' ,  views.seafoodProducts , name="fishseafood"),
#prawns products ulr
path('prawnsitems/' ,  views.prawnsProducts , name="prawns"),
#coldcuts products
path('coldcuts_items/' ,  views.coldCutProdcuts , name="coldcuts"),
#country Chicken Produts url
path('countrychicken_items/' ,  views. countryChickenProducts , name="countrychicken"),
#Pultry chicken url
path('poultrychicken_items/' ,  views.poultryChickenProducts , name="poultrychicken"),
#Ready to Cook products url
path('readytocookmeat/' ,  views.readyToCookProducts, name="readytocook"),


# Sungle product details
path('Product-details/<int:pk>/' , views.ProductDetails.as_view(), name="productdetails" ),
#add to cart
path('add-to-cart/' , views.addToCart , name="addtocart"),
#cart
path('cart/' , views.cartPage , name="cart" ),

path('checkout-cart/' , views.checkoutCart , name="checkout"),

path('our-gallery/' , views.photoGallery , name="gallery"),
path('payment-taken-here/' , views.paymentPage , name="payment"),
#search url
path('search/' ,views.searchProduct, name="search" ),

#add to wishlist
path('add-to-wishlist/', views.addToWishlist , name="addtowishlist"),
#my wishlist
path('my-wishlist',  views.myWishlist, name="mywishlist"),


#authentications urls
path('signup/' , views.SignUp.as_view() , name="signup" ),
path('accounts/login/' , auth_views.LoginView.as_view(template_name = 'myapp/login.html' , authentication_form =  LoginForm), name = "login"),
path('logout/' , auth_views.LogoutView.as_view(next_page = 'login') , name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)