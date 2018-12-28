from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from carts.models import Cart
from products.models import Product


def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    return cart_obj


def home(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        print("User is authenticated")
        print(request.user)
        request.session["cart_id"]=request.user.has_cart
        cart_id = request.session.get("cart_id", None)
        print("cart id is", cart_id)
        cart = Cart.objects.get(id=str(cart_id))
        print("Cart object is ",cart)


    cart_id = request.session.get("cart_id", None)
    print("cart id is", cart_id)


    if cart_id is None:
        if request.user.is_authenticated==False:
            print("User is not authenticated")
            cart_current=cart_create()
            request.session["cart_id"]=cart_current.id
            cart=cart_current

    else:
        cart = Cart.objects.get(id=str(cart_id))



    return render(request,"carts/home.html",context={"my_cart":cart})





def add_to_cart(request,slug):
    print("add to cart called")
    product_to_add=Product.objects.filter(slug=slug).first()
    if request.user.is_authenticated:
        cart_object=Cart.objects.get(id=int(str(request.user.has_cart)))
        cart_object.products.add(product_to_add)
    return redirect("carts:cart-home")