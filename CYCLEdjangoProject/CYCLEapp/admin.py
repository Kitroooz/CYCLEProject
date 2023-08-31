from django.contrib import admin
from .models import Seller, Item, Buyer, BuyerItem


# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        self = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if (self) and (request.user == self):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class BuyerItemAdmin(admin.TabularInline):
    model = BuyerItem
    extra = 0
    fk_name = "Buyer"


class SellerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        self = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if self and (request.user == obj.user):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'stock', 'type')
    list_filter = ('name', 'manufacturer', 'type')
    search_fields = ('name', 'manufacturer', 'type')


admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Item)
