from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    day_of_week = models.CharField(max_length=10)
    text = models.TextField(max_length=1000)
    tags = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.title} {self.date.} {self.day_of_week}'

