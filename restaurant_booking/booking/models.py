from django.db import models

from django.db import models

class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"
