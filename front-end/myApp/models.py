from django.db import models

# Create your models here.

# models.py

from django.utils import timezone

class CommNotif(models.Model):
    username = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    data = models.TextField()

    def __str__(self):
        return f'{self.username} - {self.date}'
