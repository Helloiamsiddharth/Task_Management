from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('ONGOING', 'Ongoing'),
        ("HOLDING", "Holding"),
        ('COMPLETED', 'Completed'),
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title