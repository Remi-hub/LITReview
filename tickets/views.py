from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic.detail import DetailView
from tickets.models import Ticket
from django.views.generic import ListView
from django.urls import reverse_lazy



# Create your views here.

class CreateTicket(generic.CreateView):
    model = Ticket
    success_url = reverse_lazy('home')
    template_name = 'tickets/create_ticket.html'
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



