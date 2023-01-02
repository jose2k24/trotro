# from django.db import models
from accounts.models import TrotroAccount
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
import PIL 
from PIL import Image
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.urls import reverse
from django.db.models.signals import post_save
import uuid
from django.utils import timezone
# from post.models import Post
from django.contrib.auth.decorators import login_required

# # Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='userprofile/', null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    is_bookman =models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_conductor =models.BooleanField(default=False)
    address_line_1 =  models.CharField(blank=True, max_length=120)

   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def fulladdress(self):
        return f'{self.address_line_1}-{self.address_line_2}'


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

