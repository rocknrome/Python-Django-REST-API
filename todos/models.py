from django.db import models

class Todo(models.Model):
    subject = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
