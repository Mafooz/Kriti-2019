# Generated by Django 2.2.6 on 2019-10-19 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0005_clubs_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='courses',
        ),
    ]