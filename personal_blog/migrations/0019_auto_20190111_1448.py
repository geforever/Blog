# Generated by Django 2.1.4 on 2019-01-11 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0018_auto_20190111_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 11, 6, 48, 14, 392879, tzinfo=utc)),
        ),
    ]
