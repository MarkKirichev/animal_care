from django.db import models


class Animal(models.Model):

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = [
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    ]

    name = models.CharField(max_length=20)
    image_url = models.URLField()
    description = models.TextField(max_length=250)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    is_cured = models.BooleanField(default=False)

    class Meta:
        ordering = ['priority']
