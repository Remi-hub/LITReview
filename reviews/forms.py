from django import forms
from reviews.models import Review
from django.forms import ModelForm, TypedChoiceField, RadioSelect, Select
from django.utils.safestring import mark_safe


class ReviewForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['rating'].empty_label = None

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        widgets = {
            'rating': RadioSelect
        }

