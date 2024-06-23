from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, 'Shop/catalog.html/')

def orders(request):
    return render(request, 'Shop/orders.html/')

def order_create(request):
    return render(request, 'Shop/order_create.html/')