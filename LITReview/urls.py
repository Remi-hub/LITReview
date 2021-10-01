from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('flux/', include('flux.urls')),
    path('tickets/', include('tickets.urls')),
    path('userfollows/', include('userfollows.urls')),
    path('reviews/', include('reviews.urls')),
    path('', redirect_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
