from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Detailed description of category.", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def parent_name(self):
        return self.parent.name if self.parent else "No Parent"

    @property
    def has_parent(self):
        return self.parent is not None


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveSmallIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='products')
    description = models.TextField(verbose_name="Detailed description of product.", null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
