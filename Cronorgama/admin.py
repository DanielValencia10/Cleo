from django.contrib import admin
from .models import User,Asignaturas,Proyeccion,Programas,TipoJornada,Cproyeccion,Dia,Disponibilidad,Mensajes

# Register your models here.
admin.site.register(User)
admin.site.register(Asignaturas)
admin.site.register(Proyeccion)
admin.site.register(Programas)
admin.site.register(TipoJornada)
admin.site.register(Cproyeccion)
admin.site.register(Dia)
admin.site.register(Disponibilidad)
admin.site.register(Mensajes)
