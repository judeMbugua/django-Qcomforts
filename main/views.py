from django.shortcuts import render,redirect,HttpResponse
from .models import Clothe,Order,OrderItem
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from accounts.views import signIn
import random,string
from django_daraja.mpesa.core import MpesaClient




# Create your views here.
def home(response):
    cloth = Clothe.objects.all()
    return render(response,'main/home.html',{"clothes":cloth})


def shop(request):
    clicked = False
    color = ""
    size = ""
    category = ""
    if request.method == "POST":
        clicked = True
        color = request.POST.get("filterColor")
        size = request.POST.get("filterSize")
        category = request.POST.get("filterCat")
          
    cloth = Clothe.objects.all()
    
    context = {
		"clothes":cloth,
		"clicked":clicked,
		"color":color,
		"size":size,
		"category":category,
	}
    return render(request,'main/shop.html',{"context":context})



def productInfo(request,id):
    cart = Cart(request)
    cart_products = cart.get_products()
    
    discount = 0
    
    inCart = [product.id for product in cart_products]
    product = Clothe.objects.get(id=id)
    perc_disc = 0
    #calculate discount for items on offer
    if product.offer == "yes":
        diff = (int(product.old_price) - int(product.price)) 
        discount = diff / int(product.price) * 100
      
         
        
 
    
    context = {
        'product':product,
        'inCart':inCart,
        'discount' : int(discount),
    }
    
    return render(request,'main/productInfo.html',{"context":context})




def checkout(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_products()
    totals = cart.cart_total()
    quantity = cart.get_pieces()
    cartLen = len(cart_products)
    
    
    context = {
        'cart':cart_products,
        'total':totals,
        'quantity':quantity,
        'cartLen':cartLen,
    }
    
    return render(request,'main/checkout.html',{"context":context})



@login_required(login_url = 'signIn')
def placeOrder(request):
    if request.method == "POST":
        cart = Cart(request)
        product = Clothe
        if request.POST.get("mpesa_btn"):
            code_ = request.POST.get('country_code')
            phone_number = request.POST.get('phone')
            amount = int(request.POST.get('amount').split(" ")[0])
            
            phone_number = str(code_) + str(phone_number )
            
            cl = MpesaClient()
            account_reference = 'Quality Comforts' #This is an Alpha-Numeric parameter that is defined by your system as an Identifier of the transaction for the CustomerPayBillOnline transaction type
            transaction_desc = 'shopping'
            callback_url = 'https://darajambili.herokuapp.com/express-payment';
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            

        
            
            for item in cart.get_products():   
                #get items size and quantity
                qty,size = cart.get_pieces_checkout(item.id)
                
                order = Order()
                order.product = item
                order.customer = request.user
                order.quantity = qty
                order.size = size
                order.phone = request.POST.get('phone')
                
                #generate unique tracking number
                length = 10
                chars = string.ascii_letters + string.digits
                gen1 = ''.join(random.choices(chars,k=length))
                gen2 = ''.join(random.choices(chars,k=length))
                trackNo = gen1 + gen2
                
                                
                #generate unique order_id number
                unqCode = ''.join(random.choices(chars,k=5))
                orderNo = "cat" + item.category + "usr" + str(request.user.id) + unqCode
                
                #check is order and track no unique
                while Order.objects.filter(tracking_no=trackNo) is None and Order.objects.filter(order_id=orderNo) is None :
                    trackNo = trackNo
                    orderNo = orderNo
            
                #add track and order id to model if unique
                order.tracking_no = trackNo
                order.order_id = orderNo
                order.save()
                
                #add this item to order items
                OrderItem.objects.create(
                    _order = order,
                    product = item,
                    price = item.price,
                    quantity = qty,
                )
                
                #deacrease stock count from product
                orderProduct = Clothe.objects.filter(id=item.id).first()
                updated = int(orderProduct.stockCount) - int(qty)
                orderProduct.stockCount = str(updated)
                orderProduct.save()

        
        elif request.POST.get("paypal_btn"):
            print('paypal pay')


        return redirect("shop")
    
