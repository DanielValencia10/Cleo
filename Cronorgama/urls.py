"""Cleo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, login, exit,usuarios, load_users, desactivar, asignatura, programa, modificar, desactivarpro, activarpro, modificarusu, modificarasig, modificarprom, CproyeccionU, generar, disponibilidad, asignarActividad, mensajes_recibidos, confirmar_mensaje,  proyeccion, CdisponibilidadU, rango, modificarango,enviar_disponibilidad, confirmar_disponibilidad_mensaje,salon,Cdiaedit,cronograma,CcronogramaU,Itinerario,CprogramacionU,activardis,desactivardis,obtener_opciones_filtradas,modificarcro,desactivarcro,activarcro,generar_cronograma,diligenciado,crear_tapoyo_programa#,programacion,

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('usuarios/', usuarios, name='usuarios'),
    path('logout/', exit, name='exit'),
    path('desactivar/<int:user_id>/', desactivar, name='desactivar'),
    path('user/<int:id>/', modificarusu, name='modificarusu'),
    path('table/load_users/', load_users, name='load_users'),
    path('asignatura/', asignatura, name='asignatura'),
    path('asignatura/modificar/<int:id>/', modificarasig, name='modificarasig'),
    path('programa/', programa, name='programa'),
    path('programa/modificar/<int:id>/', modificarprom, name='modificarprom'),
    path('proyeccion/', proyeccion, name='proyeccion'),
    path('proyeccion/modificar/<int:id>/', modificar, name='modificar'),
    path('proyeccion/<int:id>/generar/', generar, name='generar'),
    path('desactivarpro/', desactivarpro, name='desactivarpro'),
    path('activarpro/', activarpro, name='activarpro'),
    path('proyeccion/CproyeccionU/<int:id>/', CproyeccionU, name='CproyeccionU'),
    path('asignarActividad/', asignarActividad, name='asignarActividad'),
    path('enviar_disponibilidad/', enviar_disponibilidad, name='enviar_disponibilidad'),
    path('mensajes_recibidos/', mensajes_recibidos, name='mensajes_recibidos'),
    path('confirmar-mensaje/<int:mensaje_id>/',confirmar_mensaje, name='confirmar_mensaje'),
    path('confirmar-disponibilidad-mensaje/<int:mensaje_id>/',confirmar_disponibilidad_mensaje,name='confirmar_disponibilidad_mensaje'),
    path('diponibilidad/', disponibilidad, name='disponibilidad'),
    path('disponibilidad/Cdisponibilidad/<int:id>/', CdisponibilidadU, name='CdisponibilidadU'),
    path('disponibilidad/Cdia/<int:cdia_id>/', Cdiaedit, name='Cdiaedit'),
    path('rango/', rango, name='rango'),
    path('rango/modificar/<int:id>/', modificarango, name='modificarango'),
    path('salon/', salon, name='salon'),
    #path('programacion/', programacion, name='programacion'),
    path('cronograma/', cronograma, name='cronograma'),
    path('cronograma/CcronogramaU/<int:id>/', CcronogramaU, name='CcronogramaU'),
    path('Itinerario/', Itinerario, name='Itinerario'),
    path('Itinerario/CprogramacionU/<int:id>/', CprogramacionU, name='CprogramacionU'),
    path('desactivardis/<int:cdia_id>/', desactivardis, name='desactivardis'),
    path('activardis/<int:cdia_id>/', activardis, name='activardis'),
    path('ruta-hacia-vista/', obtener_opciones_filtradas, name='obtener_opciones_filtradas'),
    path('cronograma/bitacora/<int:id_bitacora>/', modificarcro, name='modificarcro'),
    path('desactivarcor/<int:cdia_id>/', desactivarcro, name='desactivarcro'),
    path('activarcor/<int:cdia_id>/', activarcro, name='activarcro'),
    path('cronograma/<int:id>/generar_cronograma/', generar_cronograma, name='generar_cronograma'),
    path('diligenciado/', diligenciado, name='diligenciado'),
    path('crear_tapoyo_programa/', crear_tapoyo_programa, name='crear_tapoyo_programa'),
    
]
