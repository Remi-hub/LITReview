from django.urls import path
from flux.views import events_view, personal_events_view

urlpatterns = [
    path('', events_view, name='flux'),
    path('my_posts/', personal_events_view, name='my_posts')
]
