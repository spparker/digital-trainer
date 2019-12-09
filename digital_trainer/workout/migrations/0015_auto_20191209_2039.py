# Generated by Django 2.2.8 on 2019-12-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0014_auto_20191128_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='energysystem',
            old_name='recovery',
            new_name='recovery_rec',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='movements',
        ),
        migrations.RemoveField(
            model_name='fitnesscomponent',
            name='energy_system',
        ),
        migrations.RemoveField(
            model_name='fitnesscomponent',
            name='repeat_rest',
        ),
        migrations.RemoveField(
            model_name='fitnesscomponent',
            name='req_rest',
        ),
        migrations.RemoveField(
            model_name='microcycle',
            name='modules',
        ),
        migrations.AddField(
            model_name='exercise',
            name='movement_intensity_velocity_list',
            field=models.CharField(default=[1, 50, 50], max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fitnesscomponent',
            name='intensity_max',
            field=models.IntegerField(default=75),
        ),
        migrations.AddField(
            model_name='fitnesscomponent',
            name='intensity_min',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='fitnesscomponent',
            name='req_velocity',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='energy_systems',
            field=models.ManyToManyField(to='workout.EnergySystem'),
        ),
        migrations.AddField(
            model_name='module',
            name='exercise_rest',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='recovery_time',
            field=models.IntegerField(default=24),
        ),
        migrations.AddField(
            model_name='module',
            name='repeat_time',
            field=models.IntegerField(default=48),
        ),
        migrations.RemoveField(
            model_name='microcycle',
            name='days',
        ),
        migrations.RemoveField(
            model_name='module',
            name='exercises',
        ),
        migrations.AddField(
            model_name='module',
            name='exercises',
            field=models.CharField(default=[1, 1, 2], max_length=2048),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('modules', models.ManyToManyField(to='workout.Module')),
            ],
        ),
        migrations.AddField(
            model_name='microcycle',
            name='days',
            field=models.ManyToManyField(to='workout.Day'),
        ),
    ]
