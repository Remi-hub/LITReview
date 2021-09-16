from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from dal import autocomplete
from django.shortcuts import render, redirect, get_object_or_404
from userfollows.forms import UserfollowForm, UnfollowForm
from userfollows.models import Userfollow


# Create your views here.


# class FollowsView(LoginRequiredMixin, generic.CreateView):
#     model = Userfollow
#     form_class = UserfollowForm
#     template_name = 'userfollows/follows.html'
#
#     def get_context_data(self, **kwargs):
#         # using super() to acces method (get_context_data) from CreateView
#         context = super().get_context_data(**kwargs)
#         current_user = self.request.user
#         # filter (row=...)
#         context['user_follows'] = Userfollow.objects.filter(user=current_user)
#         context['followers'] = Userfollow.objects.filter(followed_user=current_user)
#         return context


def follow_view(request):
    if request.method == 'GET':
        form_follows = UserfollowForm
        html = 'userfollows/follows.html'
        user_follows = Userfollow.objects.filter(user=request.user)
        followers = Userfollow.objects.filter(followed_user=request.user)
        context = {
            'form_follows': form_follows, 'user_follows': user_follows, 'followers': followers,
        }
        return render(request, html, context)

    elif request.method == 'POST':
        form_follows = UserfollowForm(data=request.POST, files=request.POST)
        html = 'userfollows/follows.html'
        context = {
            'form_follows': form_follows
        }
        if form_follows.is_valid():
            user = form_follows.cleaned_data['followed_user']
            current_user = request.user
            # checking if user exist and cant follow himself
            if user and user != current_user:
                # checking if the current user dosent follow the user he wants to follow
                relation_check = Userfollow.objects.filter(user=current_user).filter(followed_user=user).first()
                if not relation_check:
                    new_follow = Userfollow(user=current_user, followed_user=user)
                    new_follow.save()
                    return redirect('follows')
        return render(request, html, context)


def unfollow_view(request):
    if request.method == 'POST':
        form_unfollow = UnfollowForm(data=request.POST)
        if form_unfollow.is_valid():
            followed_user_id = form_unfollow.cleaned_data['followed_user']
            followed_user = get_object_or_404(User, id=followed_user_id)
            Userfollow.objects.get()






    # 1) determiner la personne a unfollow
    # 2) le userfollow a supprimer
    # 3) rediriger l'user sur la meme page (refresh)


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return User.objects.none()
        # targeting instance of Userfollow for the current user
        followed = list(Userfollow.objects.filter(user=self.request.user).values_list('followed_user__id', flat=True))
        qs = User.objects.exclude(id=self.request.user.id).exclude(id__in=followed)
        if self.q:
            qs = qs.filter(username__istartswith=self.q)
        return qs