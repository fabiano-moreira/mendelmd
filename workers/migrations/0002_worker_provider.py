# Generated by Django 2.0.1 on 2018-02-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='provider',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
