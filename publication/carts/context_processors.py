from .cart import Cart

"""Acess the cart in any template"""

def cart(request):
    return {'cart': Cart(request)}


