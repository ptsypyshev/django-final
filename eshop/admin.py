from django.contrib import admin
from eshop.models import Customer, Product, Order

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'created_at']
    list_filter = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'phone', 'address']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'qty','created_at']
    list_filter = ['name', 'price', 'created_at']
    search_fields = ['name', 'price', 'qty']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'created_at']
    list_filter = ['customer', 'total_price', 'created_at']
    search_fields = ['total_price']
    readonly_fields = ['created_at']
    fieldsets = (
        (None, {
            "fields": (
                "total_price",
            ),
            "classes": ["wide"],
        }),
        ("Состав заказа", {
            "fields": (
                "product",
            ),
            "description": "Продукты",
            "classes": ["collapse"],
        }),
        ("О заказе", {
            "fields": (
                'customer', 'created_at'
            )
        }),
    )
    


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)