from django.contrib import admin
from .models import Item,Cart, CartItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status',)
    search_fields = ('meal', 'description')


admin.site.register([Item, Cart, CartItem])
# admin.site.register([Item, Cart, CartItem], MenuItemAdmin)
# admin.site.register(MenuItemAdmin)
