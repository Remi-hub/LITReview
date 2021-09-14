from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms

from tickets.models import Ticket

class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "tickets/image_widget.html"


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {'image': ImageWidget}
