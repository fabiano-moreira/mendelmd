# Generated by Django 2.0.1 on 2018-02-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapps', '0003_auto_20180218_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='source',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
