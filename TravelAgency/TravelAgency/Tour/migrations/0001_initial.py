# Generated by Django 4.1.1 on 2022-09-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField(auto_now_add=True)),
                ('traveler', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Child', 'Child')], max_length=15, null=True)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('total_price', models.IntegerField()),
                ('remian', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
