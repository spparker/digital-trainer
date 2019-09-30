from django.shortcuts import render

from django.views import generic

from .models import Movement, Exercise, Module

# Full Details for a Movement
class MovementDetailView(generic.DetailView):
    model = Movement
    template_name = 'workout/movement_detail.html'

    def get_queryset(self):
        """
        Everything for now/
        """
        return Movement.objects.all()

class MovementListView(generic.ListView):
    model = Movement
    template_name = 'workout/movement_list.html'

    def get_queryset(self):
        """
        All Movements
        """
        return Movement.objects.all()

class ExerciseDetailView(generic.DetailView):
    model = Exercise
    template_name = 'workout/exercise_detail.html'

    def get_queryset(self):
        """
        All the exercises
        """
        return Exercise.objects.all()

class ExerciseListView(generic.ListView):
    model = Exercise
    template_name = 'workout/exercise_list.html'

    def get_queryset(self):
        """
        All Exercises
        """
        return Exercise.objects.all()
