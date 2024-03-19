from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Description=models.TextField()
    Published_Date=models.DateTimeField()

    def __str__(self):
        return self.name

