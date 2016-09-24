import string
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

class Alumno(models.Model):
    sede_choices = (
        ("VA", _('Villa Allende')),
        ("RO", _('Rosario')),
        ("HU", _('Hurlingham')),
        ("CR", _('Campo de la rivera')),
        ("VL", _('Villa Libertador')),
        ("MU", _('Muller')),
    )
    sede = models.CharField(choices=sede_choices, max_length=2, default="VA");
    nombre = models.CharField(max_length=80);
    apellido = models.CharField(max_length=80);
    direccion = models.CharField(max_length=80);
    barrio = models.CharField(max_length=80);
    ciudad = models.CharField(max_length=80);
    fecha_nacimiento = models.DateField(max_length=80);
    telefono = models.CharField(max_length=80,blank=True,null=True);
    telefonoFijo = models.CharField(max_length=80,null=True,blank=True);
    email = models.CharField(max_length=80,blank=True,null=True);

class Clase(models.Model):
    descripcion = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

class Asistencia(models.Model):
    fecha_hora = models.DateTimeField(auto_now=True)
    alumno = models.ForeignKey(Alumno)
    clase = models.ForeignKey(Clase)
