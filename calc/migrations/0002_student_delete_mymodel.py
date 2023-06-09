# Generated by Django 4.2 on 2023-04-09 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(default=1, editable=False, primary_key=True, serialize=False)),
                ('y1', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('y3', models.IntegerField()),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
