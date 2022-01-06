from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    query = Product.objects.all()
    one = Product.objects.get(pk=1)
    kat = Product.objects.filter(category=1)
    return HttpResponse(kat)
