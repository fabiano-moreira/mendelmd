# Generated by Django 2.0.1 on 2018-04-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='individuals',
            field=models.ManyToManyField(to='individuals.Individual'),
        ),
    ]
