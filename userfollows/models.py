from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

# Create your models here.


class Userfollow(models.Model):

    def __str__(self):
        return f'{self.user} suit {self.followed_user}'

    # suiveur
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    # le suivi
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ['user', 'followed_user']



