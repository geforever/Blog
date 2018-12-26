# Generated by Django 2.1.4 on 2018-12-25 13:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0014_auto_20181225_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_videoname',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_video_id',
            field=models.IntegerField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 13, 3, 23, 484651, tzinfo=utc)),
        ),
    ]
