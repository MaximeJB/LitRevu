from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from Tickets.models import Tickets
from django.utils.text import slugify
import uuid


class Review(models.Model):
    ticket = models.ForeignKey(to=Tickets, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.headline) or "review"
            unique = f"{base}-{uuid.uuid4().hex[:6]}"
            self.slug = unique
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
