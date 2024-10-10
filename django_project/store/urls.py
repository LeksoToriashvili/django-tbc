from django.conf.urls.static import static
from django.urls import path

from django_project import settings
from .views import categories, products

urlpatterns = [
    path('categories/', categories, name='view1'),
    path('products/', products, name='view2'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
