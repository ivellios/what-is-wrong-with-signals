from django.db import models

# Create your models here.


class ToDo(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("archived", "Archived"),
    )

    title = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return self.title
