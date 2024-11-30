from django.contrib import admin
from myapp.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    model= Category
    list_display=['id','name']

class ProductAdmin(admin.ModelAdmin):
    model= Product
    list_display=['id','name','price','categoryId']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)

