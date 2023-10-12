from django.contrib import admin

from .models import brand, Product,color,size

# Register your models here.

admin.site.register(brand)
admin.site.register(Product)
admin.site.register(color)
admin.site.register(size)