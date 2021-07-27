from django.db import models
from django.conf import settings

class Ingredient(models.Model):
    f1 = models.TextField(verbose_name='나물')
    f2 = models.TextField(verbose_name='생선')
    f3 = models.TextField(verbose_name='떡')
    f4 = models.TextField(verbose_name='국')
    f5 = models.TextField(verbose_name='면')

class FoodNutrients(models.Model):
    f1 = models.TextField(verbose_name='열량')
    f2 = models.TextField(verbose_name='탄수화물')
    f3 = models.TextField(verbose_name='단백질')
    f4 = models.TextField(verbose_name='지방')
    f5 = models.TextField(verbose_name='당류')
    f6 = models.TextField(verbose_name='콜레스테롤')

class Products(models.Model):
    f1 = models.TextField(verbose_name='채소류')
    f2 = models.TextField(verbose_name='과일류')
    f3 = models.TextField(verbose_name='곡류')

class ShoppingMall(models.Model):
    f1 = models.TextField(verbose_name='마켓컬리')
    f2 = models.TextField(verbose_name='쿠팡')
    f3 = models.TextField(verbose_name='푸드슈퍼마켓')
    f4 = models.TextField(verbose_name='G마켓')
