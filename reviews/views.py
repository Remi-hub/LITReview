from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from reviews.models import Review


# Create your views here.


class ReviewsView(LoginRequiredMixin, generic.CreateView):

    model = Review
    template_name = 'reviews/create_reviews.html'
    fields = ['headline', 'body', 'rating']
    success_url = reverse_lazy('flux')


