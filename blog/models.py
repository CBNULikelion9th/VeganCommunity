from django.db import models

# Create your models here.
class Post(models.Model):
    
    store_name =  models.CharField(max_length=100)
    location = models.TextField(default = '')
    image = models.ImageField(blank=True, upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
class Report(models.Model):
    report_title = models.CharField(max_length=100)
    report_content = models.TextField(default = '')

    def __str__(self):
        return self.title


class Save(models.Model):
    save_title = models.CharField(max_length=100)
    save__content = models.TextField(default = '')

    def __str__(self):
        return self.title


class Add(models.Model):
    add_title = models.CharField(max_length=100)
    add_content = models.TextField(default = '')
    image = models.ImageField(blank=True, upload_to='blog')

    def __str__(self):
        return self.title