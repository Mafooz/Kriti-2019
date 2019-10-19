# Generated by Django 2.2.6 on 2019-10-19 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='reg_users',
            field=models.ManyToManyField(related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='courses',
            name='shared_notes',
            field=models.ManyToManyField(related_name='courses', to='Courses.Shared_notes'),
        ),
        migrations.AlterField(
            model_name='shared_notes',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_notes', to=settings.AUTH_USER_MODEL),
        ),
    ]