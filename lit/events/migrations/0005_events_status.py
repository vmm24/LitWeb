# Generated by Django 3.2.2 on 2021-07-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210630_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.IntegerField(choices=[(0, 'Writing'), (1, 'Debating'), (2, 'Quizzing')], default=0),
            preserve_default=False,
        ),
    ]
