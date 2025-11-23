from django.forms import ModelForm
from Review.models import Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "body", "rating"]
        widgets = {
            "rating": forms.Select(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                ]
            )
        }
