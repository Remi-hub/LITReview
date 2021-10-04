from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from reviews.forms import ReviewForm
from reviews.models import Review
from tickets.forms import TicketForm
from tickets.models import Ticket


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
            form_review.instance.ticket = ticket
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
        ticket = get_object_or_404(Ticket, id=ticket_id)
        context = {
            'form_review': form_review, 'ticket': ticket,
        }

        if form_review.is_valid():
            form_review.instance.user = request.user
            form_review.instance.ticket = ticket
            form_review.save()
            return redirect('flux')

        return render(request, html, context)


def delete_review_view(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'GET':
        html = 'reviews/delete.html'
        return render(request, html)

    if request.method == 'POST':
        review.delete()
        return redirect('flux')


def edit_review_view(request, review_id,):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden()

    ticket = review.ticket
    form_review = ReviewForm(request.POST or None, instance=review)

    context = {
        'form_review': form_review, 'ticket': ticket
    }

    if request.method == 'GET':
        html = 'reviews/edit_review.html'
        return render(request, html, context)

    if form_review.is_valid():
        form_review.save()
        return redirect('flux')

    return render(request, 'reviews/edit_review.html', context)
