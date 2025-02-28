from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("name", "category")
    search_fields = ("name", "description")
