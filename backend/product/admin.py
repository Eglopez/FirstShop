from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

    list_disĺay = (
        'productName',
        'description',
        'price',
        'amount',
        'productImg',
        'productBusinessName'
    )

admin.site.register(Product,ProductAdmin,)    
