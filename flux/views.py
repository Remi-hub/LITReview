from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

# Create your views here.


def events_view(request):
    html = 'flux/flux.html'
    context = {
        'tickets': Ticket.objects.all().order_by('-time_created'),
        'reviews': Review.objects.all().order_by('-time_created')
    }

    return render(request, html, context)


def personal_events_view(request):
    html = 'flux/my_posts.html'
    current_user = request.user
    context = {
        'tickets': Ticket.objects.filter(user=current_user),
        'reviews': Review.objects.filter(user=current_user)
    }

    return render(request, html, context)


