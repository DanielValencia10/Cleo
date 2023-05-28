from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


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

class Tiposalon(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Salon(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tiposalon,blank=True, on_delete=models.CASCADE)
    capacidad = models.IntegerField(null=True, blank=True)
    habilitado=models.BooleanField(default=True,null=True)
    def __str__(self):
        return self.nombre


class Cproyeccion(models.Model):
    id = models.AutoField(primary_key=True)
    Casignatura = models.ManyToManyField(Casignatura, related_name='cproyecciones')


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
    usuario_emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    confirmar = models.BooleanField(default=True)
    usuarios_destinatarios = models.ManyToManyField(User, related_name='mensajes_recibidos')
    proyeccion = models.ForeignKey(Proyeccion, on_delete=models.CASCADE, default="", blank=True)

    def __str__(self):
        return f"Mensaje {self.id}"


class Programacion(models.Model):
    id_asignaturas = models.ForeignKey(Asignaturas, on_delete=models.CASCADE, default="", blank=True)
    id_programas = models.ForeignKey(Programas, on_delete=models.CASCADE, default="", blank=True)
    id_authuser = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True)
    id_salon = models.ForeignKey(Salon, on_delete=models.CASCADE, default="", blank=True)
    hora = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)


class Dia(models.Model):
    Nombre = models.CharField(max_length=9)

    def __str__(self):
        return self.Nombre


class Cdia(models.Model):
    dia = models.ForeignKey(Dia, max_length=200, on_delete=models.CASCADE, default="", blank=True)
    a = models.BooleanField(default=0)
    b = models.BooleanField(default=0)
    c = models.BooleanField(default=0)
    d = models.BooleanField(default=0)
    e = models.BooleanField(default=0)

class Rango(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_limite = models.DateTimeField()

class Cdisponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    cdia = models.ManyToManyField(
        Cdia, related_name='cdia')
    
    def save(self, *args, **kwargs):
        # Realizar la validación antes de guardar los datos
        if self.cdia.filter(dia=self.cdia.dia).exists():
            raise ValidationError("Ya existe un cdia con el mismo día en esta Cdisponibilidad.")
        
        super().save(*args, **kwargs)


class Disponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    Profesor = models.ForeignKey(
        User, on_delete=models.CASCADE, default="", blank=True)
    cdisponibilidad = models.ForeignKey(
        Cdisponibilidad, on_delete=models.CASCADE, default=None, blank=True, related_name='disponibilidad')

    def __str__(self):
        return f"Disponibilidad de: {self.Profesor}"


class asignaturaXprofesor(models.Model):
    id = models.AutoField(primary_key=True)
    Profesor = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True)
    Asignatura= models.ForeignKey(Asignaturas, on_delete=models.CASCADE, default="", blank=True)

    
class casigXprofe(models.Model):
    id = models.AutoField(primary_key=True)
    asigXprofe=models.ForeignKey(asignaturaXprofesor, on_delete=models.CASCADE, default="", blank=True)
    dia = models.ForeignKey(Dia, max_length=200, on_delete=models.CASCADE, default="", blank=True)
    hora_inicioClase = models.TimeField(verbose_name='Hora de inicio', blank=True)
    hora_finClase = models.TimeField(verbose_name='Hora fin', blank=True)

    def clean(self):
        if self.hora_inicioClase and self.hora_finClase:
            fecha_ficticia = datetime.now().date()
            hora_inicio = datetime.combine(fecha_ficticia, self.hora_inicioClase)
            hora_fin = datetime.combine(fecha_ficticia, self.hora_finClase)
            duracion = hora_fin - hora_inicio

            if duracion < timedelta(hours=2):
                raise ValidationError('La duración de la clase debe ser de al menos 2 horas')
            
class Ccalendario(models.Model):
    id=models.AutoField(primary_key=True)
    asigXprofe= models.ManyToManyField(casigXprofe, related_name='casigXprofe')

class calendario(models.Model):
     Programa= models.ForeignKey(Programas,on_delete=models.CASCADE,default="",blank=True)
     cCalendario=models.ForeignKey(Ccalendario, on_delete=models.CASCADE, default="", blank=True)

     def clean(self):
        if calendario.objects.filter(Programa=self.Programa).exists():
            raise ValidationError("Ya existe un calendario para este programa.")
        

class MensajesDisponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    mensaje = models.CharField(max_length=300)
    activo = models.BooleanField(default=True)
    usuario_emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_disponibilida_enviado')
    confirmar = models.BooleanField(default=True)
    usuarios_destinatarios = models.ManyToManyField(User, related_name='mensajes_disponibilidad_recibidos')
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE, related_name='mensajes')

    def __str__(self):
        return f"Mensaje de disponibilidad: {self.id}"

class Bitacora(models.Model): 
    id_bitacora = models.AutoField(primary_key=True)
    semana = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    Tema = models.CharField(max_length=300)
    material = models.CharField(max_length=200, default="")

class RegistroAsistencia(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=200, null=True)
    fecha_recuperar = models.CharField(max_length=200, null=True)
    Checkfecha_recuperar = models.BooleanField(default=False)
    tema_recuperar = models.CharField(max_length=200, null=True)
    Checktema_recuperar = models.BooleanField(default=False)
    hora_entrada = models.CharField(max_length=200, null=True)
    hora_salida = models.CharField(max_length=200, null=True)
    observaciones = models.CharField(max_length=300, default="")
    checkAsistencia=models.BooleanField(default=False)

class Ccronograma(models.Model):
    id = models.AutoField(primary_key=True)
    asignatura = models.ForeignKey(Asignaturas,on_delete=models.CASCADE, null=True, blank=True)
    bitacora = models.ManyToManyField(Bitacora, related_name='Ccronogramas')
    registroAsistencia = models.ManyToManyField(RegistroAsistencia,related_name='resgistro_de_asistencia') 

class Cronograma(models.Model):
    id = models.AutoField(primary_key=True)
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE, default=None, blank=True)
    Profesor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ccronograma = models.ForeignKey(Ccronograma, on_delete=models.CASCADE, default=None, blank=True, related_name='Cronogramas')
    activo = models.BooleanField(default=True)