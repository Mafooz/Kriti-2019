# Generated by Django 2.2.6 on 2019-10-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20191019_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='Courses',
        ),
        migrations.AddField(
            model_name='books',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='books',
            name='uploaded_by',
            field=models.CharField(max_length=2),
        ),
    ]
