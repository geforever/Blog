# Generated by Django 2.1.4 on 2019-01-11 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uservideo', '0004_auto_20190103_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservideo',
            name='video_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 11, 6, 37, 59, 846116, tzinfo=utc)),
        ),
    ]
