from django.db import models

class HeartReading(models.Model):
    min_pressure = models.IntegerField()
    max_pressure = models.IntegerField()
    heart_rate = models.IntegerField()
    reading_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reading at {self.reading_time}"
