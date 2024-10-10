from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from store.models import Category, Product


def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'categories': list(categories.values())})


def products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})
