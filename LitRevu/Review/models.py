from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from Tickets.models import Tickets


class Review(models.Model):
    ticket = models.ForeignKey(to=Tickets, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,)


#dans le models de tickets il faudrait mettre les mêmes noms genre 
#headline, body, time_created, pck sur ticket c'est title, description