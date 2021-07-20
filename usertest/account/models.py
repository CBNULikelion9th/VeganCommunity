from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, username, vegan, password=None):        
        print(111)
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = username,
            vegan = vegan
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, vegan, username, password ):        
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = username,
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
    vegan = models.CharField(
        max_length=225,
        null = False,
        unique = True
    )  
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email']
    REQUIRED_FIELDS = ['vegan']