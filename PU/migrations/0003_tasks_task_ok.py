# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PU', '0002_auto_20150930_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_ok',
            field=models.BooleanField(default=False),
        ),
    ]
