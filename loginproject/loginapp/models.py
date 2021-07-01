from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
        max_length=20,
        choices = vegan_choice,
        default='unselected'
    )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
