# Generated by Django 2.0.1 on 2018-01-08 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='S3Credential',
        ),
    ]