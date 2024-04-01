from django.contrib import admin
from Product.models import ProductModel, CustomUser

admin.site.register(ProductModel)
admin.site.register(CustomUser)
# Register your models here.
