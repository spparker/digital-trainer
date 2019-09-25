from django.urls import path

from . import views
from . import models

app_name = 'workout'
urlpatterns = [
        # ex: /workout/movement/
        ## TODO: Create index views
        path('movement/', views.MovementListView.as_view(),
             name='movement_list'),
        # ex: /workout/movement/3
        path('movement/<int:pk>/', views.MovementDetailView.as_view(), name='movement_detail'),
    path('movement/<slug:DIFFICULTY_CHOICES>/',
         views.MovementListView.as_view(), name='movement_list'),
]
