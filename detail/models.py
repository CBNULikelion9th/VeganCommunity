from django.db import models
from django.conf import settings

class Vegan(models.Model):
    f1 = models.TextField(default="밀가루")
    f2 = models.TextField(default="돼지고기")
    f3 = models.TextField(default="닭가슴살")
    f4 = models.TextField(default="채소")

class Ingredient(models.Model):
    f1 = models.TextField(default="샐러드")
    f2 = models.TextField(default="건강식")
    f3 = models.TextField(default="계란")
    f4 = models.TextField(default="바지락")

class Product(models.Model):
    f1 = models.TextField(default="샐러드")
    f2 = models.TextField(default="프로틴")
    f3 = models.TextField(default="찌개")
    f4 = models.TextField(default="저칼로리")

class Shopping(models.Model):
    f1 = models.TextField(default="단백질")
    f2 = models.TextField(default="탄수화물")
    f3 = models.TextField(default="반찬가게")
    f4 = models.TextField(default="다이어트 식단")
