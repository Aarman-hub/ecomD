from django.contrib import admin

from products.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','parent','description']
	list_filter = ['status']



class ProductAdmin(admin.ModelAdmin):
	list_display = ['title','price','description','images']
	list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)