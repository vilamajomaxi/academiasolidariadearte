# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20160924_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='tipo',
            field=models.CharField(default=b'DS', max_length=2, choices=[(b'DS', 'Devolucion solidaria'), (b'CV', 'Consolidacion de valores'), (b'R', 'Clase regular')]),
        ),
    ]
