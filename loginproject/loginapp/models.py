from django.db import models

class join(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name