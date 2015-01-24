# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0002_auto_20150124_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='appointmentdate',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 24, 7, 57, 18, 620472)),
        ),
    ]
