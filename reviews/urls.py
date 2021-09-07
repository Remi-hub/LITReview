from django.urls import path
from reviews.views import ReviewsView



urlpatterns = [
    path('create_review/', ReviewsView.as_view(), name='create_reviews'),
]
