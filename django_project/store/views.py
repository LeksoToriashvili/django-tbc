from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from store.models import Category, Product
from django.db.models import F, Sum


def get_all_subcategories(category, visited=None):
    if visited is None:
        visited = set()

    if category in visited:
        return []

    visited.add(category)

    subcategories = category.children.all()
    all_subcategories = list(subcategories)

    for subcategory in subcategories:
        all_subcategories.extend(get_all_subcategories(subcategory, visited))

    return all_subcategories


def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'categories': list(categories.values())})


def products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})


def category(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'main_category_listing.html', {'categories': categories})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    all_subcategories = get_all_subcategories(category)
    category_names = [name for name in all_subcategories]
    products = Product.objects.filter(category__name__in=category_names)
    prices = list(products.values_list('price', flat=True))
    print(prices)
    expensive = max(prices)
    cheap = min(prices)
    avg = sum(prices) / len(prices)
    total = products.aggregate(total=Sum(F('price') * F('quantity')))['total']

    return render(request, 'category_product_listing.html', {
        'category': category.name,
        'products': products,
        'expensive': expensive,
        'cheap': cheap,
        'avg': avg,
        'total': total,
    })


def product_details(request, product_id):
    product = Product.objects.prefetch_related('category').get(id=product_id)
    return render(request, 'product_details.html', {'product': product})
