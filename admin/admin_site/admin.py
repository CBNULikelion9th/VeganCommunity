from django.contrib import admin
from .models import User, Vegan_Store, Store_Review, Food,\
                    Food_Review, Market_Goods,Goods_Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authority')
    fields = ('__all__',)

class VeganStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'vegan_step')
    fields = ('__all__',)

class CustomStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    fields = ('__all__',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('__all__',)

class MarketGoodsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'food_name',)
    fields = ('__all__',)

admin.site.register(User, UserAdmin)
admin.site.register(Vegan_Store, VeganStoreAdmin)
admin.site.register(Store_Review)
admin.site.register(Food, FoodAdmin)
admin.site.register(Food_Review)
admin.site.register(Market_Goods, MarketGoodsAdmin)
admin.site.register(Goods_Comment)