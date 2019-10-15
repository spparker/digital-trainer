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

#class StrengthMovement(Movement):
    #TODO: Add equipment
    #Equipment = models.ManyToManyField(Equipment)

#class ConditioningMovement(Movement):
#    bytime = models.BooleanField() # by time?
#    value = models.IntegerField() #seconds or meters

#    def __str__(self):
#        if self.bytime():
#            return "Conditioning Movement: " + self.name + " for " + self.value
#            + "seconds"
#        else:
#            return "Conditioning Movement: " + self.name + " " + self.value 
#            + "meters"

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


class Module(models.Model):
    name = models.CharField(max_length=512)
    exercises = models.ManyToManyField(Exercise)
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

