# Generated by Django 2.1.4 on 2018-12-24 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('personal_blog', '0003_auto_20181221_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=256)),
                ('video_path', models.CharField(default=None, max_length=400)),
                ('video_update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 8, 20, 36, 976152, tzinfo=utc)),
        ),
    ]
