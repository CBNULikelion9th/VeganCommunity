from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100, default="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='blog/', null=True)
    #question = models.ForeignKey(Question, Null=True, blank=True ,on_delete=models.CASCADE) 
    #answer = models.ForeignKey(Answer, Null=True, blank=True, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)


    def __str__(self): 
        return f'{self.title}'

# from django.utils import timezone
# #장고에서 기본으로 제공되는 timezone을 import 해줌

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self): 
        return self.comment


