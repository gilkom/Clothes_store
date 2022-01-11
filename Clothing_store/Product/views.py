from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


def index(request):
    query = Product.objects.all()
    one = Product.objects.get(pk=1)
    kat = Product.objects.filter(category=1)
    man = Product.objects.filter(manufacturer=2)
    categories = Category.objects.all()
    # categories = Product.objects.filter(category__isnull=False)
    contains = Product.objects.filter(description__icontains='bla')
    data = {'categories': categories}
    return render(request, 'indek.html', data)


def category(request, id):
    category_user = Category.objects.get(pk=id)
    category_product = Product.objects.filter(category = category_user)
    categories = Category.objects.all()
    data = {'category_user': category_user, 'category_product': category_product, 'categories': categories}
    return render(request, 'category_product.html', data)


def product(request, id):
    product_user = Product.objects.get(pk=id)
    categories = Category.objects.all()
    data = {'product_user': product_user, 'categories': categories }
    return render(request, 'product.html', data)
