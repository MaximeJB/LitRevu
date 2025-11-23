from django.db import models
from django.contrib.auth.models import AbstractUser


class UserApp(AbstractUser):
    blocked_user = models.ManyToManyField(
        "self", symmetrical=False, related_name="Blocked_by"
    )

    def __str__(self):
        return self.username
