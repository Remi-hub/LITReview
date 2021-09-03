from django.urls import path
from userfollows.views import FollowsView


urlpatterns = [
    path('follows/', FollowsView.as_view(), name='follows')
]