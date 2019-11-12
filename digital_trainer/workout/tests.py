from django.test import TestCase
from workout.models import Movement, Exercise, Module

# Create your tests here.

def setUp(self):
    Movement.objects.create(name="Bilateral Vertical Jump", description="Stand"
                            "on two legs and jump straight up",
                            difficulty=Movement.INTERMEDIATE,
                            video='')

    Movement.objects.create(name="Bilateral Broad Jump", description="Stand"
                            "on two legs and jump forward",
                            difficulty=Movement.INTERMEDIATE,
                            video='')


    Movement.objects.create(name="Bilateral Squat", description="Stand on two"
                            "legs and squat down until thighs are near parallel",
                            difficulty=Movement.BEGINNER,
                            video='')

    Movement.objects.create(name="Unilateral Skater Squat", description="Stand"
                            "on one leg, tilt pelvis forward, and bend the"
                            "standing leg as the raised leg extends and"
                            "counterblances the forward tilt",
                            difficulty=Movement.INTERMEDIATE,
                            video='')

    Movement.objects.create(name="Run", description="Linear Bilateral"
                            "Movement", difficulty=Movement.BEGINNER,
                            video="")

    Movement.objects.create(name="Freestyle Swim", description="Linear swim"
                            "using any stroke",
                            difficulty=Movement.INTERMEDIATE,
                            video="")

    mo = [Movement.objects.create(name="200m Sprint", description="Running near"
                                 "top speed for 200 meters.",
                                 difficulty=Movement.BEGINNER,
                                 video="")]

    Movement.objects.create(name="Change Direction", description="Plant and"
                           "change direction", difficulty=Movement.INTERMEDIATE,
                           video="")

    e = Exercise.objects.create(name="200m Repeats", description="multiple 200s",
                            sets = 2, reps = 4,
                            rep_rest_absolute = False,
                            work_ratio = 1, rest_ratio = 3, set_rest = 180)
    e.movements.set(mo)

    e = Exercise.objects.create(name="200m Repeats fixed rest",
                            description="multiple 200s",
                            sets = 1, reps = 6,
                            rep_rest_absolute = True,
                            absolute_rep_rest = 30,
                            set_rest = 0)
    e.movements.set(mo)
