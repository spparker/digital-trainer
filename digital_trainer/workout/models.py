from django.db import models


# Create your models here.
class Movement(models.Model):
    BEGGINER = 'BEG'
    INTERMEDIATE = 'INT'
    ADVANCED = 'ADV'
    DIFFICULTY_CHOICES = [
            (BEGGINER, 'Begginer'),
            (INTERMEDIATE, 'Intermediate'),
            (ADVANCED, 'Advanced'),
    ]
    name = models.CharField(max_length=256)
    description = models.TextField
    video = models.URLField(max_length=1024)
    difficulty = models.CharField(
            max_length=3,
            choices=DIFFICULTY_CHOICES,
            default=INTERMEDIATE,
    )


class Exercise(models.Model):
    name = models.CharField(max_length=512)
    movements = models.ManyToManyField(Movement)
    sets = models.IntegerField()
    set_rest = models.IntegerField() #seconds
    reps = models.IntegerField()
    rep_rest_absolute = models.BooleanField()
    absolute_rep_rest = models.IntegerField() #seconds
    work_ratio = models.IntegerField()
    rest_ratio = models.IntegerField()


class Workout(models.Model):
    name = models.CharField(max_length=512)
    exercises = models.ManyToManyField(Exercise)
