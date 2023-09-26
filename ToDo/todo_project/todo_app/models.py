
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

