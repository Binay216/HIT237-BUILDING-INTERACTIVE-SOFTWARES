from django.db import models
from django.contrib.auth.models import User

class RepairRequest(models.Model):
    ISSUE_TYPES = [
        ('AC', 'Air Conditioning'),
        ('PLUMBING', 'Plumbing'),
        ('ELECTRICAL', 'Electrical'),
        ('DOOR', 'Door/Lock'),
        ('ROOF', 'Roof'),
        ('OTHER', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('EMERGENCY', 'Emergency'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_REVIEW', 'In Review'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='LOW')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    image = models.FileField(upload_to='repairs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"