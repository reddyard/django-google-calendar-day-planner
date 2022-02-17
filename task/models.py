from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    notification_date = models.DateTimeField(blank=True, null=True)

    def schedule(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
