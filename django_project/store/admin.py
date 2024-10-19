from django.contrib import admin
from store.models import Category, Product
from store.views import products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_parent', 'parent', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'image')
    list_per_page = 10
    list_filter = ('category',)
