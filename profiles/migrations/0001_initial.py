# Generated by Django 2.2.10 on 2023-04-01 04:54

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='customers/profiles/avatars/')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('institution', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('yearofjoining', models.DateField(blank=True, null=True)),
                ('phd', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Yes'), (2, 'NO')], null=True)),
                ('qualifications', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
