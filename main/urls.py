from django.urls import path
from . import views

urlpatterns = [
	path("",views.home,name="home"),
	path("home/",views.home,name="home"),
	path("shop/",views.shop,name="shop"),
 	path("checkout/",views.checkout,name="checkout"),
  	path("place-order/",views.placeOrder,name="placeOrder"),
  	path("contact/",views.sendEmail,name="sendEmail"),
	path("product/<int:id>/",views.productInfo,name="productInfo"),			
 

]