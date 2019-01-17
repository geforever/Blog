# Generated by Django 2.1.4 on 2019-01-17 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0020_auto_20190117_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 8, 13, 35, 734090, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_video_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
