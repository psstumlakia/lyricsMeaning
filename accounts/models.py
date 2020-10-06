from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(interests='a')


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    interests = models.CharField(max_length=200, default='')
    nickname = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):  # keyword arguments
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)  # if a user is created automatically a user profile is created
