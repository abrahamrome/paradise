# Generated by Django 3.2.7 on 2022-03-11 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paradise_app', '0004_auto_20220310_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 12, 31, 45, 294253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 12, 31, 45, 294253, tzinfo=utc)),
        ),
    ]
