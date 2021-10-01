from reviews.models import Review
from django.forms import ModelForm, RadioSelect


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        widgets = {
            'rating': RadioSelect
        }
