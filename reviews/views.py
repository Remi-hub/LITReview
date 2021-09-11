from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from reviews.models import Review
from reviews.forms import ReviewForm
from tickets.forms import TicketForm
from tickets.views import CreateTicket
from tickets.models import Ticket
from django.shortcuts import get_object_or_404


# Create your views here.

def review_create_view(request):
    if request.method == 'GET':
        form_review = ReviewForm()
        form_ticket = TicketForm()
        html = 'reviews/create_reviews.html'
        context = {
            'form_review': form_review, 'form_ticket': form_ticket
        }
        return render(request, html, context)

    elif request.method == 'POST':
        form_review = ReviewForm(data=request.POST, files=request.FILES)
        form_ticket = TicketForm(data=request.POST, files=request.FILES)

        html = 'reviews/create_reviews.html'
        context = {
            'form_review': form_review, 'form_ticket': form_ticket
        }

        if form_review.is_valid() and form_ticket.is_valid():
            form_ticket.instance.user = request.user
            ticket = form_ticket.save()
            form_review.instance.ticket = ticket    #ticket dans le model review
            form_review.instance.user = request.user
            form_review.save()

            return redirect('flux')

        return render(request, html, context)



def review_create_view_with_ticket(request, ticket_id):

    if request.method == 'GET':
        form_review = ReviewForm()
        ticket = get_object_or_404(Ticket, id=ticket_id)
        html = 'reviews/create_review_with_ticket.html'
        context = {
            'form_review': form_review, 'ticket': ticket,
        }
        return render(request, html, context)

    elif request.method == 'POST':
        form_review = ReviewForm(data=request.POST, files=request.FILES)
        html = 'reviews/create_review_with_ticket.html'
        context = {
            'form_review': form_review,
        }

        if form_review.is_valid():
            form_review.instance.user = request.user
            form_review.save()
            return redirect('flux')

        return render(request, html, context)


