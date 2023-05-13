from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta


class User(AbstractUser):
    emailI = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class TipoJornada(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre


class Programas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    jornada = models.ForeignKey(TipoJornada, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre+" "+self.jornada.nombre


class Asignaturas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    creditos = models.IntegerField()
    intensidad = models.IntegerField()
    semestre = models.IntegerField()
    programa = models.ForeignKey(
        Programas, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.codigo+" "+self.nombre


class Casignatura(models.Model):
    id = models.AutoField(primary_key=True)
    asignaturas = models.ForeignKey(Asignaturas, on_delete=models.CASCADE, related_name='cproyecciones')
    total_semanas = models.IntegerField(null=True, blank=True)
    num_docentes = models.IntegerField(null=True, blank=True, default=0)


class Salon(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    capacidad = models.IntegerField(null=True, blank=True)


class Cproyeccion(models.Model):
    id = models.AutoField(primary_key=True)
    Casignatura = models.ManyToManyField(
        Casignatura, related_name='cproyecciones')


class Proyeccion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    semestre = models.PositiveIntegerField()
    programas = models.ForeignKey(
        Programas, on_delete=models.CASCADE, default=None, blank=True)
    cproyeccion = models.ForeignKey(
        Cproyeccion, on_delete=models.CASCADE, default=None, blank=True, related_name='proyecciones')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Proyeccion de: {self.programas.nombre}"

    # def save(self, *args, **kwargs):
    #     if self.programas != self.Cproyeccion.self
    #         raise ValueError("la proyeccion solo acepta asignaturas relacionadas con El tipo de proyeccion")
    #     super().save(*args, **kwargs)


class Mensajes(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    mensaje = models.CharField(max_length=300)
    activo = models.BooleanField(default=True)
    usuario_emisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    confirmar = models.BooleanField(default=True)
    usuarios_destinatarios = models.ManyToManyField(
        User, related_name='mensajes_recibidos')
    proyeccion = models.ForeignKey(
        Proyeccion, on_delete=models.CASCADE, default="", blank=True)

    def __str__(self):
        return f"Mensaje {self.id}"


class Programacion(models.Model):
    id_asignaturas = models.ForeignKey(
        Asignaturas, on_delete=models.CASCADE, default="", blank=True)
    id_programas = models.ForeignKey(
        Programas, on_delete=models.CASCADE, default="", blank=True)
    id_authuser = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", blank=True)
    id_salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, default="", blank=True)
    hora = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)


class Bitacora(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    id_authuser = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", blank=True)
    id_programas = models.ForeignKey(
        Programas, on_delete=models.CASCADE, default="", blank=True)
    id_asignaturas = models.ForeignKey(
        Asignaturas, on_delete=models.CASCADE, default="", blank=True)
    semana = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    Tema = models.CharField(max_length=200)


class RegistroAsistencia(models.Model):

    fecha = models.CharField(max_length=200)
    semana = models.CharField(max_length=200)
    fecha_recuperar = models.CharField(max_length=200)
    tema_recuperar = models.CharField(max_length=200)
    total_hora = models.CharField(max_length=200)
    hora_entrada = models.CharField(max_length=200)
    hora_salida = models.CharField(max_length=200)
    id_bitacora = models.ForeignKey(
        Bitacora, on_delete=models.CASCADE, default="", blank=True)


class Dia(models.Model):
    Nombre = models.CharField(max_length=9)

    def __str__(self):
        return self.Nombre


class Cdia(models.Model):
    dia = models.ForeignKey(Dia, max_length=200,
                            on_delete=models.CASCADE, default="", blank=True)
    a = models.BooleanField(default=0)
    b = models.BooleanField(default=0)
    c = models.BooleanField(default=0)
    d = models.BooleanField(default=0)
    e = models.BooleanField(default=0)


class Cdisponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    cdia = models.ManyToManyField(
        Cdia, related_name='cdia')


class Disponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    Profesor = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", blank=True)
    cdisponibilidad = models.ForeignKey(
        Cdisponibilidad, on_delete=models.CASCADE, default=None, blank=True, related_name='disponibilidad')
    fecha_inicio = models.DateTimeField(default=datetime.now)
    fecha_fin = models.DateTimeField(
        default=datetime.now() + timedelta(days=7))
    def __str__(self):
        return f"Disponibilidad de: {self.Profesor}"
