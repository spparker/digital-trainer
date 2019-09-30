# Generated by Django 2.2.4 on 2019-09-30 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('workout', '0006_auto_20190930_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditioningMovement',
            fields=[
                ('movement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workout.Movement')),
                ('bytime', models.BooleanField()),
                ('value', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('workout.movement',),
        ),
        migrations.AlterModelOptions(
            name='movement',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='movement',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_workout.movement_set+', to='contenttypes.ContentType'),
        ),
    ]
