from django.contrib import admin
from pages .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug', ]
    prepopulated_fields = {'slug': ('category_name',)}



admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'is_available', ]
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ['is_available']


admin.site.register(Product, ProductAdmin)
