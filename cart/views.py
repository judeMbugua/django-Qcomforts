from django.shortcuts import render,get_object_or_404
from .cart import Cart
from main.models import Clothe
from django.http import JsonResponse


def cart_summary(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_products()
    quants = cart.get_quants()
    totals = cart.cart_total()
    
    offers = {}
    
    for item in cart_products:
        if item.offer == "yes":
            diff = (int(item.old_price) - int(item.price)) 
            discount = diff / int(item.price) * 100
            
            offers[item.id] = int(discount)
           
    

    
    context = {
        "cart_products":cart_products,
        'quant':quants,
        'offers':offers,
        'totals':totals,

    }
    
    
    
    return render(request,"cart/cart_summary.html",{"context":context})







def cart_add(request):
    #get the cart
    cart = Cart(request)
    
    #test for post
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product_size = request.POST.get('product_size')
        
        #lookup product in the database
        product = get_object_or_404(Clothe,id=product_id) #get the object,if not found return 404 error
        
        #save product to session;add to cart
        cart.add(product=product,quantity=product_qty,size=product_size)
        
        #get cart quantity
        cart_quantity = cart.__len__()
        
        #return response
        response = JsonResponse({'id':cart_quantity })
        return response
    
    
def cart_update(request):
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = request.POST.get('prd_id')
        product_qty = request.POST.get('prd_qty')
        product_size = request.POST.get('prd_size')

        
        
        cart.update(product=product_id,quantity=product_qty,size=product_size)
        
        response = JsonResponse({"qty":product_qty})
        return response
    
    
def cart_remove(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        
    cart.remove(product=product_id)
    
    
    response = JsonResponse({"id":product_id})
    return response