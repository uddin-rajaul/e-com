from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, ProductLine

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
