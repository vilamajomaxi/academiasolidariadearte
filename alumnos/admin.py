from django.contrib import admin
from .models import Alumno, Clase, Asistencia

class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','sede','barrio','ciudad')

class ClaseAdmin(admin.ModelAdmin):
	list_display = ('titulo','sede','descripcion',)

class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ('fecha_hora','alumno','clase')


#Agregado de control de admin y relacion de parametros
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)


# Register your models here.
