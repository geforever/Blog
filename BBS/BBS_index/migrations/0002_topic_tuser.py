# Generated by Django 2.1.4 on 2019-01-24 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('BBS_index', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='topic',
            name='tUser',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
