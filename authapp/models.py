from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    actvation_key = models.CharField(max_length=128, blank=True)
    actvation_key_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def is_activation_key_expired(self):
        if now() < self.actvation_key_created + timedelta(hours=48):
            return False
        return True