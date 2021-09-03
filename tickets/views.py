from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tickets.models import Ticket


# Create your views here.
class CreateTicket(LoginRequiredMixin, generic.CreateView):
    model = Ticket
    success_url = reverse_lazy('home')
    template_name = 'tickets/create_ticket.html'
    fields = ['title', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





