# Generated by Django 2.0.1 on 2018-02-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_params'),
        ('analyses', '0002_analysis_apps'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='files',
            field=models.ManyToManyField(to='files.File'),
        ),
    ]
