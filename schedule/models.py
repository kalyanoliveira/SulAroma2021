from django.db import models
import datetime

# Create your models here.

# Event SQL database table. Columns: name, starting date, ending date, description
class event(models.Model):
    name = models.CharField(max_length=64)
    whenStart = models.DateTimeField()
    whenEnd = models.DateTimeField()
    description = models.TextField()

    def __str__ (self):
        return f"{self.name}, {self.whenStart} - {self.whenEnd}"