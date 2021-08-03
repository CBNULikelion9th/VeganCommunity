from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# 로그인 User
class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, username, vegan, password=None):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            username = username,
            vegan = vegan
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, vegan, username, password ):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            username = username,
            vegan = vegan,         
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,
        null=False,        
        unique=True,    
    )    
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    
    unselected = 'us'
    vegan = 'vg'
    lacto = 'lt'
    ovo = 'ov'
    lacto_ovo = 'lov'
    pesco = 'pc'
    flexiterian = 'fx'


    vegan_choice = (
        (unselected, 'unselected'),
        (vegan, 'vegan'),
        (lacto, 'lacto'),
        (ovo, 'ovo'),
        (lacto_ovo, 'lacto_ovo'),
        (pesco, 'pesco'),
        (flexiterian, 'flexiterian'),
    )
    
    vegan = models.CharField(
        max_length=225,
        unique=False,
        choices=vegan_choice
    )  

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['vegan', 'email']

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