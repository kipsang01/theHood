from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    profile_pic = CloudinaryField('image')
    neigborhood = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return str(self.user)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Neigborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)