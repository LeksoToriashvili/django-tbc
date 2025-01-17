from django.conf.urls.static import static
from django.urls import path

from django_project import settings
from .views import categories, products, category, category_products, product_details

urlpatterns = [
    path('categories/', categories, name='view1'),
    path('products/', products, name='view2'),
    path('category/', category, name='category'),
    path('category/<int:category_id>/products/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_details, name='product_details'),
]
