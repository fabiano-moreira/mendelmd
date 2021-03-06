# Generated by Django 2.0.1 on 2018-01-08 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='S3Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('access_key', models.CharField(max_length=255)),
                ('secret_key', models.CharField(max_length=255)),
                ('buckets', models.TextField(blank=True, null=True)),
                ('exclude_paths', models.TextField(blank=True, null=True)),
                ('exclude_files', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
