from django.db import models
from django.conf import settings

class Category(models.Model):
    f1 = models.ManyToManyField("self")
    f2 = models.ManyToManyField("self")
    f3 = models.ManyToManyField("self")
    f4 = models.ManyToManyField("self")

