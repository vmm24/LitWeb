# Generated by Django 3.2.4 on 2021-06-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210624_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]
