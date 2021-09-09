from django.urls import path
from flux.views import events_view

urlpatterns = [
    path('', events_view, name='flux'),
]
