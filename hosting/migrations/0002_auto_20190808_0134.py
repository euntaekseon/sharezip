# Generated by Django 2.2.4 on 2019-08-07 16:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 7, 16, 34, 59, 781994, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 7, 16, 34, 59, 781994, tzinfo=utc)),
        ),
    ]
