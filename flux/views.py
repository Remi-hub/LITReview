from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from itertools import chain

# Create your views here.


"""
Afficher les tickets & les reviews 
nous allons devoir faire une query sur ces objets
faire une boucle sur le template pour parcourir tous nos objets ( tickets & reviews )

"""

def events_view(request):
    html = 'flux/flux.html'
    context = {
        'tickets': Ticket.objects.all().order_by('-time_created'), 'reviews': Review.objects.all().order_by('-time_created')
    }

    return render(request, html, context)


