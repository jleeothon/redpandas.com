# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('redpanda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redpanda',
            name='cuteness',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(3)]),
        ),
    ]
