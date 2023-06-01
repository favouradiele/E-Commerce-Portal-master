# Generated by Django 2.0.2 on 2018-02-25 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180225_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='book image url', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_created',
            field=models.DateField(verbose_name=datetime.datetime(2018, 2, 25, 16, 57, 38, 516261)),
        ),
    ]
