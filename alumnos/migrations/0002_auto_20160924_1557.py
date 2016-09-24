# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora', models.DateTimeField(auto_now=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='asistencia',
            name='clase',
            field=models.ForeignKey(to='alumnos.Clase'),
        ),
    ]
