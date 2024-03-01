from main.models import Clothe 

class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get("session_key")

        # if the user is new,no session key! create one!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product,quantity,size):
        product_id = str(product.id)
        product_qty = str(quantity)
        product_size = size

        # logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {
                "qty": int(product_qty),
                "size": product_size,
            }  # a dict with id as key and dict of price as value

        self.session.modified = True

    # this func returns the length of the cart dict;total number of products in the cart

    def __len__(self):
        return len(self.cart)



    def get_products(self):
        #get ids currently in the cart
        product_ids = self.cart.keys()
        
        #use id's to lookup products in db models
        products = Clothe.objects.filter(id__in=product_ids)
        
        #return the looked up products
        return products
    

    def get_quants(self):
        q = self.cart
        return q
    
    def get_pieces(self):
        cart_ = self.cart
        
        for key,val in cart_.items():
            for k,v in val.items():
                if k == "qty":
                    qty = v
        
        return qty
    
    def get_pieces_checkout(self,id):
        cart_ = self.cart
        
        for key,val in cart_.items():
            if key == str(id):
                for k,v in val.items():
                    if k == "qty":
                        qty = v
                    if k == "size":
                        size = v
        
        return qty,size
    
    
    def update(self,product,quantity,size):
        _id = product
        _qty = quantity
        _size = size

        
        #get cart
        CurrCart = self.cart
      
        
        #update dict
        CurrCart[_id] = {
                "qty": _qty,
                "size": _size,
            } 
        
        
        self.session.modified = True
        
        
    def remove(self,product):
        id = str(product)
        
        cart_ = self.cart
        
        if id in cart_:
            del cart_[id]
            
        self.session.modified = True
                
                
    def cart_total(self):
        cart_ids = self.cart.keys()  #get keys of items in the cart dict(session)
        
        products = Clothe.objects.filter(id__in=cart_ids)  #get those products that are in cart from db model
        
        cart_ = self.cart
        
        total = 0
        
        for key,val in cart_.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total += (int(product.price) * int(val["qty"]) )
                    
                    
        return total
    
    