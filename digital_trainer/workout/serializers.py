from rest_framework import serializers
from workout.models import Movement, Exercise, Module, Microcycle, Mesocycle, Macrocycle

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        #fields = ('id', 'name', 'description', 'difficulty', 'unilateral',
        #          'video_url')
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class MicrocycleSerializer(serializers.ModelSerializer):
     class Meta:
         model = Microcycle
         fields = '__all__'
