from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from importlib import import_module
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

# Create your models here.
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


    vegan_choice = [
        (unselected, 'unselected'),
        (vegan, 'vegan'),
        (lacto, 'lacto'),
        (ovo, 'ovo'),
        (lacto_ovo, 'lacto_ovo'),
        (pesco, 'pesco'),
        (flexiterian, 'flexiterian'),
    ]
    
    vegan = models.CharField(
        
        max_length=225,
        unique=False
    )  

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['vegan', 'email']

SessionStore=import_module(settings.SESSION_ENGINE).SessionStore

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

def block_duplicate_logins(sender, request, user, **kwargs):
    for user_session in UserSession.objects.filter(user=user):
        session_key = user_session.session_key
        session = SessionStore(session_key)
        session.delete()
    session_key = request.session.session_key
    UserSession.objects.create(user=user, session_key=session_key)
    user_logged_in.connect(block_duplicate_logins)