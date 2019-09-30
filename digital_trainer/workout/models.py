from django.db import models


# Create your models here.
class Movement(models.Model):
    BEGINNER = 'BEG'
    INTERMEDIATE = 'INT'
    ADVANCED = 'ADV'
    DIFFICULTY_CHOICES = [
            (BEGINNER, 'Beginner'),
            (INTERMEDIATE, 'Intermediate'),
            (ADVANCED, 'Advanced'),
    ]
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    video = models.URLField(max_length=1024)
    difficulty = models.CharField(
            max_length=3,
            choices=DIFFICULTY_CHOICES,
            default=INTERMEDIATE,
    )
    def __str__(self):
        return self.name



class Exercise(models.Model):
    name = models.CharField(max_length=512)
    movements = models.ManyToManyField(Movement)
    description = models.CharField(max_length=2048)
    sets = models.IntegerField()
    set_rest = models.IntegerField(default=0) #seconds
    reps = models.IntegerField()
    rep_rest_absolute = models.BooleanField()
    absolute_rep_rest = models.IntegerField(default=None, blank=True,
                                            null=True) #seconds
    work_ratio = models.IntegerField(default=None, blank=True, null=True)
    rest_ratio = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=512)
    exercises = models.ManyToManyField(Exercise)
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

