from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Market_Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100, default="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='blog/', null=True)

    def __str__(self): 
        return f'{self.title}'

class Market_Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Market_Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self): 
        return self.comment


