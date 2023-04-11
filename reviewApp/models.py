from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    type = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('issue-detail', kwargs={'pk': self.pk})


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    # Add any other fields you need for the Contact model.

    def __str__(self):
        return self.name
