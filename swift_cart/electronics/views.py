# Create your views here.
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    cart_items = request.session.get('cart', [])

    total = sum(item['price'] for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def add_to_cart(request, name, price):
    cart = request.session.get('cart', [])

    cart.append({
        'name': name,
        'price': int(price)
    })

    request.session['cart'] = cart

    return redirect('/cart/')

def remove_from_cart(request, index):
    cart = request.session.get('cart', [])

    if 0 <= index < len(cart):
        cart.pop(index)

    request.session['cart'] = cart

    return redirect('/cart/')