from django.db import models

# Create your models here.
class Post(models.Model):
    
    store_name =  models.CharField(max_length=100)
    reportcontent = models.TextField(default = '')
    location = models.TextField(default = '')
    image = models.ImageField(blank=True, upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'