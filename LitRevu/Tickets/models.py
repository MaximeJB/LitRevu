from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid


class Tickets(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "ticket"
            unique = f"{base}-{uuid.uuid4().hex[:6]}"
            self.slug = unique
        super().save(*args, **kwargs)
