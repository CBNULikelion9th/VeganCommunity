from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

STEP = (
    ('100% 비건', '100% 비건'),
    ('일부 비건', '일부 비건'),
)

STORE = (
    ('음식점', '음식점'),
    ('화장품', '화장품'),
    ('카페', '카페'),
)

FEATURE = (
    ('Halal 인증', 'Halal 인증'),
    ('Vegan', 'Vegan'),
    ('사찰 음식', '사찰 음식'),
)

GOODS_FEATURE = (
    ('농산물', '농산물'),
    ('제철 과일', '제철 과일'),
    ('기타', '기타'),
)

class User(models.Model):
    authority = models.CharField(max_length=10, choices=(('master', 'master'), ('user', 'user'),))
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    vegan_step = models.CharField(max_length=10, choices=STEP, blank=True)

class Vegan_Store(models.Model):
    name = models.CharField(max_length=50)
    vegan_step = models.CharField(max_length=10, choices=STEP)
    address = models.CharField(max_length=100)
    field = models.CharField(max_length=10, choices=STORE)

class Store_Review(models.Model):
    store = models.ForeignKey(Vegan_Store, on_delete=models.CASCADE, related_name='reviews')
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()

class User_Custom_Store(models.Model):
    name = models.CharField(max_length=50)
    vegan_step = models.CharField(max_length=10, choices=STEP)
    address = models.CharField(max_length=100)
    field = models.CharField(max_length=10, choices=STORE)

class Food(models.Model):
    name = models.CharField(max_length=50)
    all_nutrition = models.TextField()
    allegy_nutrition = models.TextField()
    Feature = MultiSelectField(choices=FEATURE, blank=True)
    # 주소, 대체품 리스트 형태로 구현

class Food_Review(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='review')
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()

class Market_Goods(models.Model):
    user_name = models.CharField(max_length=50)
    food_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    feature = models.CharField(max_length=10, choices=GOODS_FEATURE)
    content = models.TextField()

class Goods_Comment(models.Model):
    goods = models.ForeignKey(Market_Goods, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=50)
    comment = models.TextField()