from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
