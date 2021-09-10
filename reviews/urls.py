from django.urls import path
from reviews.views import review_create_view
from reviews.views import review_create_view_with_ticket



urlpatterns = [
    path('create_review/', review_create_view, name='create_reviews'),
    path('create_review_with_ticket/<int:ticket_id>/', review_create_view_with_ticket, name='create_review_with_ticket'),

]
