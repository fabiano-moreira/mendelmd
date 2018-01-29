# Generated by Django 2.0.1 on 2018-01-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('n_tasks', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(max_length=30)),
                ('current_status', models.TextField(blank=True, null=True)),
                ('worker_id', models.CharField(max_length=30)),
                ('ip', models.CharField(max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('started', models.DateTimeField(null=True)),
                ('finished', models.DateTimeField(null=True)),
                ('execution_time', models.TimeField(null=True)),
            ],
        ),
    ]
