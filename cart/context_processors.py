from .cart import Cart

#create context processors so that cart can work on all site pages

def cart(request):
    #return default data from the cart
    return {
        'cart':Cart(request)
    }
    