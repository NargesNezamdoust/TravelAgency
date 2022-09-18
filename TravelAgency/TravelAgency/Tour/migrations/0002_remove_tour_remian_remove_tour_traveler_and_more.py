# Generated by Django 4.1.1 on 2022-09-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='remian',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='traveler',
        ),
        migrations.AddField(
            model_name='tour',
            name='traveler_adult',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='traveler_child',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]