# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Client
 

    """
    when the Client model is saved, a signal is fired called create_profile which creates a Profile instance with a foreign key pointing to the instance of the user.
    """
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance, name=instance.username)
  
