from django.urls import path
from reviews.views import review_create_view



urlpatterns = [
    path('create_review/', review_create_view, name='create_reviews'),
]
