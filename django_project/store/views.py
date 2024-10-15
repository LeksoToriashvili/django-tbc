from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from store.models import Category, Product


def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'categories': list(categories.values())})


def products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})


def category(request):
    categories = Category.objects.all()
    return render(request, 'main_category_listing.html', {'categories': categories})


def category_products(request, category_id):
    l = []
    parent_category = Category.objects.get(id=category_id)
    subcategories = parent_category.children.all()

    return JsonResponse({'all_products': list(subcategories.values())})
