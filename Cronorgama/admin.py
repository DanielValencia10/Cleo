from django.contrib import admin
from .models import User,Asignaturas,Proyeccion,Programas,TipoJornada,Cproyeccion,Dia,Disponibilidad,Mensajes,Tiposalon,Cdisponibilidad,Cdia, MensajesDisponibilidad,Cronograma,Ccronograma,RegistroAsistencia,Bitacora,Grupo,BDcontratista,Programacion

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
admin.site.register(Tiposalon)
admin.site.register(Cdisponibilidad)
admin.site.register(Cdia)
admin.site.register(MensajesDisponibilidad)
admin.site.register(Cronograma)
admin.site.register(Ccronograma)
admin.site.register(RegistroAsistencia)
admin.site.register(Bitacora)
admin.site.register(Grupo)
admin.site.register(BDcontratista)
admin.site.register(Programacion)