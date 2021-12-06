from django.shortcuts import render, redirect
from .models import Product, Category

# Create your views here.
def index(request):
    if request.method =="POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('Session', request.session['cart'])
        return redirect('index')
    products = None
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    context = {'products': products, 'categories': categories}
    return render(request, 'product/index.html', context)

def cart(request):
    listid = list(request.session.get('cart').keys())
    cartitems = Product.get_products_by_id(listid)
    print(cartitems)
    return render(request, 'product/cart.html',{'cartitems':cartitems})