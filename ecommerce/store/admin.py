from django.contrib import admin
from store.models import Product,Category,Cart,CartItem
# Register your models here.
#,'created','updated'
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','created']
    list_editable = ['price','stock']
    list_per_page = 5

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)