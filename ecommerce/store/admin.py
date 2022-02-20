from django.contrib import admin
from store.models import Product,Category,Cart,CartItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)