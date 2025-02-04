from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255, verbose_name='Title')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium', verbose_name='Priority')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Active', verbose_name='Status')
    due_date = models.DateField(null=True, blank=True, verbose_name='Due Date')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
