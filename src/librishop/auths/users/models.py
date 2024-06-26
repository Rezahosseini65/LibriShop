from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=32, null=True, blank=True)
    lastname = models.CharField(max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=1024, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['province']),
            models.Index(fields=['city']),
        ]
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return f'{self.user} >> {self.user.email}'


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
