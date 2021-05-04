from django.shortcuts import render
from store.models import Product

def home(request):
    products    = Product.objects.all().filter(is_available=True) #Only Bring Those Products that are True

    context = {
        'products': products,
    }
    return render(request,'home.html', context)
