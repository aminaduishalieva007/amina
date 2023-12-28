from django.shortcuts import render
from product.models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request,
                'index.html',
                context={'products': products}
                )