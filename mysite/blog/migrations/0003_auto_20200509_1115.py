# Generated by Django 3.0.3 on 2020-05-09 05:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200509_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 5, 30, 45, 775898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 5, 30, 45, 771898, tzinfo=utc)),
        ),
    ]
