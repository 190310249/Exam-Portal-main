# Generated by Django 3.1.3 on 2022-05-26 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20220519_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 14, 1, 37, 24189)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 14, 1, 37, 24189)),
        ),
    ]
