from django.urls import path
from tickets.views import CreateTicket


urlpatterns = [
    path('create_ticket/', CreateTicket.as_view(), name='create_ticket')
]