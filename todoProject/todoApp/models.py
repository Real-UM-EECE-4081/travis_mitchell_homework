from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=200, null=True, blank=True)  # New field for category
    expected_time_to_complete = models.DurationField(null=True, blank=True)  # New field for expected time to complete
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)  # New field for completed
    completion_date = models.DateField(null=True, blank=True)  # New field for completion date
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    objects = models.Manager()

    def __str__(self):
        return self.description
