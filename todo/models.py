from django.db import models


class Todo(models.Model):
    """Model to represent list of todo activites"""
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=150, help_text="describe what you want to do", null=True)
    date_time = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} @ {self.date_time}"

