from django.urls import path

from . import views

app_name = 'workout'
urlpatterns = [
        # ex: /workout/movement/
        ## TODO: Create index views
        # ex: /workout/movement/3
        path('movement/<int:pk>/', views.MovementDetailView.as_view(), name='movement_detail'),
]

