# Generated by Django 3.2.4 on 2021-06-24 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='author',
        ),
        migrations.RemoveField(
            model_name='events',
            name='status',
        ),
        migrations.AlterField(
            model_name='events',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
