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
    movement_intensity_velocity_list = models.CharField(max_length=2048) #[[Movement_id, percent_effort, velocity]]
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

    def set_movement_intensity_veloicty_list(self, x):
        self.movement_intensity_velocity_list = json.dumps(x)

    def get_movement_intensity_velocity_list(self):
        return json.loads(self.movement_intensity_velocity_list)

class EnergySystem(models.Model):
    name = models.CharField(max_length=512)
    activation = models.IntegerField(default=0)
    duration = models.IntegerField(default=30)
    recovery_rec = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FitnessComponent(models.Model):
    name = models.CharField(max_length=512)
    req_velocity = models.IntegerField(default=50)
    intensity_min = models.IntegerField(default=50)
    intensity_max = models.IntegerField(default=75)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=512)
    exercises = models.CharField(max_length=2048)
    exercise_rest = models.IntegerField(default=0)
    description = models.CharField(max_length=2048)
    fitness_components = models.ManyToManyField(FitnessComponent)
    energy_systems = models.ManyToManyField(EnergySystem)
    recovery_time = models.IntegerField(default=24)
    repeat_time = models.IntegerField(default=48)

    def __str__(self):
        return self.name

    def set_exercises(self, x):
        self.exercises = json.dumps(x)

    def get_exercises(self):
        return json.loads(self.exercises)

    #def exercise_names(self):
    #    return ', '.join([e.name for e in self.exercises.all()])
    #exercise_names.short_description = "Exercise Names"

class Day(models.Model):
    number = models.IntegerField()
    modules = models.ManyToManyField(Module)

class Microcycle(models.Model):
    name = models.CharField(max_length=512)
    days = models.ManyToManyField(Day)

    def __str__(self):
        return self.name + ':  ' + str(self.days)

class Mesocycle(models.Model):
    name = models.CharField(max_length=512)
    fitness_components = models.ManyToManyField(FitnessComponent)
    energy_systems = models.ManyToManyField(EnergySystem)
    days = models.IntegerField(default=28)
    microcycles = models.ManyToManyField(Microcycle)

    def __str__(self):
        return self.name

class Macrocycle(models.Model):
    name = models.CharField(max_length=512)
    days = models.IntegerField(default=180)
    mesocycles = models.ManyToManyField(Mesocycle)

    def __str__(self):
        self.name + ' ' + str(self.days) + ' days'

class TrainingDay(models.Model):
    date = models.DateField()
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return date


