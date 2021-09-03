from django.urls import path
from userfollows.views import FollowsView
from .views import UserAutocomplete
# from your_countries_app.views import CountryAutocomplete


urlpatterns = [
    path('follows/', FollowsView.as_view(), name='follows'),
    path('user_autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete')
]
