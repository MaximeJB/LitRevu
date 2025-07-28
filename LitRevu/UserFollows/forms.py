from django.forms import ModelForm, CharField
from .models import UserFollows


class FollowForm(ModelForm):
    username = CharField(required=False, label="Search User")

    class Meta:
        model = UserFollows
        fields = ("username",)
