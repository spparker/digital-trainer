from django.urls import path

from . import views
from . import models

app_name = 'workout'
urlpatterns = [
        path('workout/movement/', views.MovementListView.as_view(),
             name='movement_list'),
        ## ex: /workout/movement/3
        path('workout/movement/<int:pk>/', views.MovementDetailView.as_view(), name='movement_detail'),
        path('workout/movement/<slug:DIFFICULTY_CHOICES>/',
         views.MovementListView.as_view(), name='movement_list'),
        ## ex: /workout/exercise/
        path('workout/exercise/', views.ExerciseListView.as_view(),
             name='exercise_list'),
        ## ex: /workout/exercise/2
        path('workout/exercise/<int:pk>/', views.ExerciseDetailView.as_view(),
             name='exercise_detail'),
        path('workout/module/<int:pk>/', views.ModuleDetailView.as_view(),
             name='module_detail'),
        path('workout/module/', views.ModuleListView.as_view(),
             name='module_list'),
        path('workout/cycle/<int:pk>/', views.CycleDetailView.as_view(),
             name='cycle_detail'),
        path('workout/cycle/', views.CycleListView.as_view(),
             name='cycle_list'),
        ## API
        path('api/movement/', views.MovementListCreate.as_view() ),
        path('api/exercise/', views.ExerciseListCreate.as_view() ),
        path('api/module/', views.ModuleListCreate.as_view() ),
        path('api/microcycle/', views.MicrocycleListCreate.as_view() ),
]
