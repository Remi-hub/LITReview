from django import forms
from reviews.models import Review
from django.forms import ModelForm, TypedChoiceField, RadioSelect


choices = (
    (0, '0'),
    (1, '1')
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = 'headline', 'rating', 'body'

