from django.db import models
from Review.models import Review
from django.conf import settings


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    ) 
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
