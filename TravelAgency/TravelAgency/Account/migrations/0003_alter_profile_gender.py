# Generated by Django 4.1.1 on 2022-09-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman'), ('NoGender', 'NoGender')], max_length=10),
        ),
    ]
