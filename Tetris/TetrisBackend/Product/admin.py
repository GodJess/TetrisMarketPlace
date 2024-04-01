from django.contrib import admin
from Product.models import ProductModel, CustomUser, SalesMan, Snikers, cloth

admin.site.register(ProductModel)
admin.site.register(CustomUser)
admin.site.register(cloth)
admin.site.register(SalesMan)
admin.site.register(Snikers)
# Register your models here.
