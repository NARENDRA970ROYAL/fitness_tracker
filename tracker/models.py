from django.db import models

class FitnessTracker(models.Model):
    exercise = models.CharField(max_length=100)
    duration = models.IntegerField()   # in minutes
    calories_burned = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.exercise