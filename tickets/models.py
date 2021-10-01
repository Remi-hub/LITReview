from django.conf import settings
from django.db import models
# from reviews.models import Review

# Create your models here.


class Ticket(models.Model):
    title = models.CharField(verbose_name='Nom du ticket', max_length=128)
    description = models.TextField(max_length=2048, blank=True,
                                   verbose_name='Description du ticket')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='tickets')
    time_created = models.DateTimeField(auto_now_add=True)

    def has_review(self):
        return self.reviews.exists()

    def tickets_from_current_user(self):
        return Ticket.objects.filter(user=self.user)
