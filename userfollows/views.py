from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from dal import autocomplete

from userfollows.forms import UserfollowForm
from userfollows.models import Userfollow


# Create your views here.


class FollowsView(LoginRequiredMixin, generic.CreateView):
    model = Userfollow
    form_class = UserfollowForm
    template_name = 'userfollows/follows.html'

    def get_context_data(self, **kwargs):
        # using super() to acces method (get_context_data) from CreateView
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        # filter (row=...)
        context['user_follows'] = Userfollow.objects.filter(user=current_user)
        context['followers'] = Userfollow.objects.filter(followed_user=current_user)
        return context


    #
    # def get_form_kwargs(self):
    #     form = super().get_form_kwargs()
    #

    # def follow(self):
    #     current_user = self.request.user
    #     user_followers = Userfollow.objects.filter()
    #     if current_user.followers
    #
    #     pass

    # le current user doit pouvoir suivre la personne qu'il a cibler
    # if user is not in  related_name = following
    # -> user.add() -> following




class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return User.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(username__istartswith=self.q)

        return qs