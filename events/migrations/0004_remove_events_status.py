# Generated by Django 3.2.2 on 2021-06-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_events_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='status',
        ),
    ]