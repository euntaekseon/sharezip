# Generated by Django 2.2.4 on 2019-08-07 16:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime(2019, 8, 7, 16, 33, 37, 792677, tzinfo=utc))),
                ('end_date', models.DateField(default=datetime.datetime(2019, 8, 7, 16, 33, 37, 793205, tzinfo=utc))),
                ('rent_type', models.IntegerField(default=-1)),
                ('roomate_num', models.IntegerField(default=-1)),
                ('building_type', models.IntegerField(default=-1)),
                ('period', models.IntegerField(default=-1)),
                ('cost', models.IntegerField(default=-1)),
                ('university', models.IntegerField(default=-1)),
                ('gender', models.IntegerField(default=-1)),
                ('addr_gu', models.CharField(max_length=20)),
                ('addr_dong', models.CharField(max_length=20)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
                ('detail', models.TextField(default='')),
                ('deposit', models.IntegerField(default=-1)),
                ('rooms', models.IntegerField(default=-1)),
                ('options', jsonfield.fields.JSONField(default={'air_conditioner': 0, 'bed': 0, 'closet': 0, 'desk': 0, 'doorlock': 0, 'duplex': 0, 'induction': 0, 'tv': 0, 'washer': 0, 'wifi': 0})),
                ('address', models.CharField(default=' ', max_length=50)),
                ('address_detail', models.CharField(default=' ', max_length=50)),
                ('creator', models.CharField(max_length=150)),
            ],
        ),
    ]
