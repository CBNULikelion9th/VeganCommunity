from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authority')
    fields = ('__all__',)

class VeganStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'vegan_step')
    fields = ('__all__',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('__all__',)

class MarketGoodsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'food_name',)

admin.site.register(User, UserAdmin)
admin.site.register(Vegan_Store, VeganStoreAdmin)
admin.site.register(Store_Review)
admin.site.register(Food, FoodAdmin)
admin.site.register(Food_Review)
admin.site.register(Market_Goods, MarketGoodsAdmin)
admin.site.register(Goods_Comment)