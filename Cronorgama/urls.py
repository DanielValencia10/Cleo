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
from .views import home, login, exit, table, load_users, desactivar, asignatura, programa, modificar, desactivarpro, activarpro, modificarusu, modificarasig, modificarprom, CproyeccionU, generar, disponibilidad, enviar_tarea, mensajes_recibidos, confirmar_mensaje,  proyeccion, CdisponibilidadU

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('table/', table, name='table'),
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
    path('proyeccion/CproyeccionU/<int:id>/',
         CproyeccionU, name='CproyeccionU'),
    path('enviar-tarea/', enviar_tarea, name='enviar_tarea'),
    path('mensajes_recibidos/', mensajes_recibidos, name='mensajes_recibidos'),
    path('confirmar-mensaje/<int:mensaje_id>/',
         confirmar_mensaje, name='confirmar_mensaje'),
    path('diponibilidad/', disponibilidad, name='disponibilidad'),
    path('disponibilidad/Cdisponibilidad/<int:id>/',
         CdisponibilidadU, name='CdisponibilidadU'),
]
