# Generated by Django 2.2.4 on 2019-09-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_auto_20190918_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='description',
            field=models.CharField(default='jump', max_length=2048),
            preserve_default=False,
        ),
    ]
