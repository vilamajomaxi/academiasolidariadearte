import string
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

sede_choices = (
    ("VA", _('Villa Allende')),
    ("RO", _('Rosario')),
    ("HU", _('Hurlingham')),
    ("CR", _('Campo de la rivera')),
    ("VL", _('Villa Libertador')),
    ("MU", _('Muller')),
)

tipo_choices = (
    ("DS", _('Devolucion solidaria')),
    ("CV", _('Consolidacion de valores')),
    ("R", _('Clase regular')),
)

class Alumno(models.Model):

    sede = models.CharField(choices=sede_choices, max_length=2, default="VA")
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    barrio = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(max_length=80)
    telefono = models.CharField(max_length=80,blank=True,null=True)
    telefonoFijo = models.CharField(max_length=80,null=True,blank=True)
    email = models.CharField(max_length=80,blank=True,null=True)


    def __str__(self):
        return str(self.nombre) + " "+str(self.apellido)

class Clase(models.Model):
    titulo = models.CharField(max_length=60,null=False)
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    sede = models.CharField(choices=sede_choices, max_length=2, default="VA")
    tipo =  models.CharField(choices=tipo_choices, max_length=2, default="DS")

    def __str__(self):
        return str(self.descripcion) + "-"+str(self.sede)

class Asistencia(models.Model):
    fecha_hora = models.DateTimeField(auto_now=True)
    alumno = models.ForeignKey(Alumno)
    clase = models.ForeignKey(Clase)
