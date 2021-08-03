from django.db import models
from django.conf import settings

# user_custom store
class Post(models.Model):
    
    store_name =  models.CharField(max_length=100)
    reportcontent = models.TextField(default = '')
    location = models.TextField(default = '')
    image = models.ImageField(blank=True, upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

# 농산물 market
class Market_Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100, default="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='market', null=True)
    view_count = models.IntegerField(default=0)


    def __str__(self): 
        return f'{self.title}'

class Market_Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self): 
        return self.comment