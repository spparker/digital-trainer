from django.test import TestCase
from workout.models import Movement, Exercise, Workout

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

    Movement.objects.create(name="Change Direction", description="Plant and"
                           "change direction", difficulty=Movement.INTERMEDIATE,
                           video="")

