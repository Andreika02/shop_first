from django.shortcuts import redirect, render
from .models import Product, Order
# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'Shop/catalog.html/', {"products": products})

def orders(request):
    if not request.user.is_authenticated:
        return redirect("signin")
    orders = Order.objects.filter(user = request.user)
    return render(request, 'Shop/orders.html/', {"orders": orders})

# def order_create(request):
#     if not request.user.is_authenticated:
#         return redirect("signin")
#     return render(request, 'Shop/order_create.html/')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'Shop/product_detail.html', {"product": product})

def order_create(request, product_id):
    if not request.user.is_authenticated:
        return redirect("signin")
    product = Product.objects.get(id=product_id)
    print(request.user)
    if request.method == "POST":
        Order.objects.create(
            product = product,
            adress = request.POST.get("adress"),
            user = request.user 
        )
        return redirect("catalog")
    return render(request, 'Shop/order_create.html', {"product": product})
