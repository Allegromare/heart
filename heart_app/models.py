from django.db import models

class HeartReading(models.Model):
    min_pressure = models.IntegerField()
    max_pressure = models.IntegerField()
    heart_rate = models.IntegerField()
    reading_date = models.DateField(auto_now_add=True)
    reading_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"Reading at {self.reading_date} {self.reading_time}"
