# Generated by Django 2.1.4 on 2019-01-03 04:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0016_auto_20190103_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 3, 4, 56, 7, 516931, tzinfo=utc)),
        ),
    ]
