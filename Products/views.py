from django.shortcuts import render
from .models import ProductInfo
# Create your views here.


def home_page(request):
    products = ProductInfo.objects.all()
    return render(request, 'Products/home.html', {'products': products})
