from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Movement, Exercise, Module

admin.site.register(Movement)
admin.site.register(Exercise)

#class MovementChildAdmin(PolymorphicChildModelAdmin):
#    base_model = Movement

    #base_fieldsets = [
    #    (None,         {'fields': ['Name']}),
    #    (None,         {'fields': ['Description']}),
    #    (None,         {'fields': ['Video']}),
    #]

#@admin.register(ConditioningMovement)
#class ConditioningMovementAdmin(MovementChildAdmin):
#    base_model = ConditioningMovement
#    show_in_index = True

#@admin.register(Movement)
#class MovementParentAdmin(PolymorphicParentModelAdmin):
#    base_model = Movement
#    child_models = (ConditioningMovement,)
#    list_filter = (PolymorphicChildModelFilter,)

