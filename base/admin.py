from django.contrib import admin
from .models import Product
from .models import ProductDetails,ProductDetailsUK,ProductDetailsCA,ProductDetailsUS
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource 

# Register your models here.

#admin.site.register(Product)
admin.site.register(ProductDetails)
admin.site.register(ProductDetailsUS)
admin.site.register(ProductDetailsCA)
admin.site.register(ProductDetailsUK)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("asin","title", "image", "price","deal")
    #resource_class = ProductResource

#admin.site.register(Product, ProductAdmin)



