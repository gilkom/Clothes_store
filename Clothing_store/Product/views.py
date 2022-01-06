from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


def index(request):
    query = Product.objects.all()
    one = Product.objects.get(pk=1)
    kat = Product.objects.filter(category=1)
    man = Product.objects.filter(manufacturer=2)
    cat_name = Category.objects.get(id=4)
    categories = Product.objects.filter(category__isnull=False)
    contains = Product.objects.filter(description__icontains='bla')
    data = {'categories': categories}
    return render(request, 'indek.html', data)


def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user)
