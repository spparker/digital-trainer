from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
#class Movement(PolymorphicModel):
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
    unilateral = models.BooleanField(default=False)
    video = models.URLField(max_length=1024, default=None, blank=True,
                            null=True)
    difficulty = models.CharField(
            max_length=3,
            choices=DIFFICULTY_CHOICES,
            default=INTERMEDIATE,
    )
    #TODO: Intensity needs to be inside a persons scheduled workout
    #intensity = models.IntegerField(max = 100) #percent effort / speed
    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=512)
    movements = models.ManyToManyField(Movement)
    description = models.CharField(max_length=2048)
    sets = models.IntegerField()
    set_rest = models.IntegerField(default=0) #seconds
    reps = models.IntegerField()
    rep_length = models.IntegerField(default=0) #seconds/meters
    absolute_rep_rest = models.IntegerField(default=None, blank=True,
                                            null=True) #seconds / -1 for ratio
    work_ratio = models.IntegerField(default=None, blank=True, null=True)
    rest_ratio = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class EnergySystem(models.Model):
    name = models.CharField(max_length=512)
    activation = models.IntegerField(default=0)
    duration = models.IntegerField(default=30)
    recovery = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FitnessComponent(models.Model):
    name = models.CharField(max_length=512)
    req_rest = models.IntegerField(default=24)
    repeat_rest = models.IntegerField(default=48)
    energy_system = models.ManyToManyField(EnergySystem)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=512)
    exercises = models.ManyToManyField(Exercise)
    description = models.CharField(max_length=2048)
    fitness_components = models.ManyToManyField(FitnessComponent)
    energy_systems = models.ManyToManyField(EnergySystem)

    def __str__(self):
        return self._check_long_column_names

    #def exercise_names(self):
    #    return ', '.join([e.name for e in self.exercises.all()])
    #exercise_names.short_description = "Exercise Names"

class Day(models.Model):
    date = models.DateField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return date


