from django.shortcuts import render
from tickets.models import Ticket
from reviews.models import Review
from userfollows.models import Userfollow
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain

# Create your views here.


def events_view(request):
    html = 'flux/flux.html'
    # user = follower
    followed_users = list(Userfollow.objects.filter(user=request.user).values_list('followed_user__id', flat=True))
    followed_users.append(request.user.id)
    context = {
        'tickets': Ticket.objects.filter(user__id__in=followed_users).order_by('-time_created'),
        'reviews': Review.objects.filter(Q(user__id__in=followed_users) |
                                         Q(ticket__user=request.user)).order_by('-time_created')
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


