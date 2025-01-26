from django.db import models

class HeartReading(models.Model):
    min_pressure = models.IntegerField()
    max_pressure = models.IntegerField()
    heart_rate = models.IntegerField()
    reading_date = models.DateTimeField()
 
    def __str__(self):
        return f"Reading at {self.reading_date}"
