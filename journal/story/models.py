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

    text = models.TextField(max_length=5000)
    tags = models.TextField(max_length=50, blank=True)

    def __str__(self):
        # see if have event that lasted several days
        if self.date_start == self.date_end:
            return f"{self.date_start.strftime('%d %B %Y')} {self.title} {self.day_of_week_start}"
        else:
            return f"{self.date_start.strftime('%d')}-{self.date_end.strftime('%d %B %Y')} {self.title} {self.day_of_week_start}"


