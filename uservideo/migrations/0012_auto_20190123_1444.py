# Generated by Django 2.1.4 on 2019-01-23 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uservideo', '0011_auto_20190123_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='video_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 6, 44, 47, 62023, tzinfo=utc)),
        ),
    ]