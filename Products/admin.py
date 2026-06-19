from django.contrib import admin
from .models import ProductInfo
# Register your models here.


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']