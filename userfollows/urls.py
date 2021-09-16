from django.urls import path
from userfollows.views import follow_view, unfollow_view
from .views import UserAutocomplete
# from your_countries_app.views import CountryAutocomplete


urlpatterns = [
    path('unfollows/', unfollow_view, name="unfollows"),
    path('follows/', follow_view, name='follows'),
    path('user_autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete')
]
