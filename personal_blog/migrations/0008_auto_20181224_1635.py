# Generated by Django 2.1.4 on 2018-12-24 08:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0007_auto_20181224_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 8, 35, 8, 652866, tzinfo=utc)),
        ),
    ]
