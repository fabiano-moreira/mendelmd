# Generated by Django 2.0.1 on 2018-04-14 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import samples.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('is_featured', models.BooleanField(default=True)),
                ('is_public', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, help_text='File Format: VCF', max_length=600, upload_to=samples.models.Sample.get_upload_path)),
                ('file_header', models.TextField(blank=True, null=True)),
                ('prefix', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, editable=False, max_length=100)),
                ('n_variants', models.IntegerField(blank=True, editable=False, null=True)),
                ('n_lines', models.IntegerField(blank=True, editable=False, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.ManyToManyField(blank=True, to='files.File')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SampleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(related_name='samplegroup_members', to='samples.Sample')),
            ],
        ),
    ]
