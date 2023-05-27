from django.contrib import admin
from .models import User,Asignaturas,Proyeccion,Programas,TipoJornada,Cproyeccion,Dia,Disponibilidad,Mensajes,Tiposalon,Cdisponibilidad,Cdia, MensajesDisponibilidad

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

