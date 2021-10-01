from django.urls import path
from tickets.views import CreateTicket, EditTicket, DeleteTicket

urlpatterns = [
    path('create_ticket/', CreateTicket.as_view(), name='create_ticket'),
    path('edit/<int:pk>/', EditTicket.as_view(), name='edit_ticket'),
    path('delete/<int:pk>/delete', DeleteTicket.as_view(),
         name='delete_ticket')
]
