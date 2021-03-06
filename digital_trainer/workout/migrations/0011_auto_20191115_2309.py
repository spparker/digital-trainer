# Generated by Django 2.2.4 on 2019-11-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0010_movement_unilateral'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergySystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('activation_start', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=30)),
                ('recovery_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('req_rest', models.IntegerField(default=24)),
                ('repeat_rest', models.IntegerField(default=48)),
                ('energy_system', models.ManyToManyField(to='workout.EnergySystem')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('modules', models.ManyToManyField(to='workout.Module')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='energy_systems',
            field=models.ManyToManyField(to='workout.EnergySystem'),
        ),
        migrations.AddField(
            model_name='module',
            name='fitness_components',
            field=models.ManyToManyField(to='workout.FitnessComponent'),
        ),
    ]
