from django.db import models
import datetime

# have curr_date since it is referenced in many of the fields
class Entry(models.Model):
    curr_date = datetime
    title = models.CharField(max_length=100)
    date_start = models.DateField(default=curr_date.datetime.today().date())
    date_end = models.DateField(default=curr_date.datetime.today().date())

    day_of_week_start = models.CharField(max_length=10, default=curr_date.datetime.today().strftime("%A"))
    day_of_week_end = models.CharField(max_length=10, default="", blank=True)

    text = models.TextField(max_length=1000)
    tags = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.title} {self.date_start} {self.day_of_week_start}'

