from django.shortcuts import render
from .models import Product

def main (request):
    product_list = Product.objects.all()

    return render(request, 'mainapp/index.html', context={'user':{'name': 'oleg', 'surname': 'vahrameev'}, 'products': product_list})

def products (request, pk=None):
    print(pk)
    return render(request, 'mainapp/products.html')

def contacts (request):
    return render(request, 'mainapp/contacts.html')