# Generated by Django 2.1.4 on 2019-01-24 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uservideo', '0013_auto_20190124_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='video_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 6, 52, 35, 353131, tzinfo=utc)),
        ),
    ]
