# Generated by Django 5.0.1 on 2024-01-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_remove_doctor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='timing1',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='timing2',
            field=models.TimeField(default='17:00'),
        ),
    ]
