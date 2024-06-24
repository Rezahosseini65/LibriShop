from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .validators import phone_number_validator, postal_code_validator


# Create your models here.


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, null=True, blank=True,
                                    validators=[
                                        phone_number_validator,
                                    ])
    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True,
                                   validators=[
                                       postal_code_validator
                                   ])

    class Meta:
        indexes = [
            models.Index(fields=['province']),
            models.Index(fields=['city']),
        ]
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
