from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def show(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'show.html', {'product': product})