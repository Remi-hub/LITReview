from django.forms import ModelForm
from django import forms

from tickets.models import Ticket


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "tickets/image_widget.html"


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'image': ImageWidget, 'description':
                forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
