from django.contrib import admin
from textiles.models import Product, ProductImage, SubProduct, Order, Address, PaytmHistory
# Register your models here.
class PaytmHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'MID', 'TXNAMOUNT', 'STATUS')


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(SubProduct)
admin.site.register(Order)
admin.site.register(Address)

admin.site.register(PaytmHistory, PaytmHistoryAdmin)


