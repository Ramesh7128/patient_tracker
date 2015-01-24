# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='appointmentdate',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 5, 54, 57, 866317)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patients',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 5, 55, 10, 994952), auto_now_add=True),
            preserve_default=False,
        ),
    ]
