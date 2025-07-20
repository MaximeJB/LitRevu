from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Tickets(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank = True)
    time_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,)

   