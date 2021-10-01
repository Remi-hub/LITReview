from django.urls import path
from reviews.views import review_create_view, review_create_view_with_ticket,\
    edit_review_view, delete_review_view

urlpatterns = [
    path('create_review/', review_create_view, name='create_reviews'),
    path('create_review_with_ticket/<int:ticket_id>/',
         review_create_view_with_ticket,
         name='create_review_with_ticket'),
    path('edit_review/<int:review_id>/', edit_review_view, name='edit_review'),
    path('delete/<int:review_id>/', delete_review_view, name="delete_review")
]
