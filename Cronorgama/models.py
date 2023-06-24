from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    emailI = models.EmailField(null=True, blank=True)
    cedula= models.IntegerField(null=True, blank=True)

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

class Dia(models.Model):
    Nombre = models.CharField(max_length=9)

    def __str__(self):
        return self.Nombre

class HorarioDia(models.Model):
    dia = models.ForeignKey(Dia, max_length=200, on_delete=models.CASCADE, default="", blank=True)
    a = models.BooleanField(default=0)
    b = models.BooleanField(default=0)
    c = models.BooleanField(default=0)
    d = models.BooleanField(default=0)
    e = models.BooleanField(default=0)
    activo= models.BooleanField(default=True)

class Rango(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_limite = models.DateTimeField()

class HorarioProfesor(models.Model):
    id = models.AutoField(primary_key=True)
    cdia = models.ManyToManyField(HorarioDia, related_name='cdia')
    

class Disponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    Profesor = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True)
    cdisponibilidad = models.ForeignKey(HorarioProfesor, on_delete=models.CASCADE, default=None, blank=True,related_name='disponibilidad')

    def __str__(self):
        return f"Disponibilidad de: {self.Profesor}"
        
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
    bitacora = models.ManyToManyField(Bitacora, related_name='Ccronogramas')
    registroAsistencia = models.ManyToManyField(RegistroAsistencia,related_name='resgistro_de_asistencia') 

class Cronograma(models.Model):
    id = models.AutoField(primary_key=True)
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE, default=None, blank=True)
    Profesor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ccronograma = models.ForeignKey(Ccronograma, on_delete=models.CASCADE, default=None, blank=True, related_name='Cronogramas')
    asignatura = models.ForeignKey(Asignaturas,on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField(default=True)

class BDcontratista(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=11)
    def __str__(self):
        return f" {self.nombre}"
    
class Grupo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=3)
    def __str__(self):
        return f" {self.nombre}"

class Programacion(models.Model):
    id_asignaturas = models.ForeignKey(Asignaturas, on_delete=models.CASCADE, default="", blank=True)
    id_authuser = models.ForeignKey(User, on_delete=models.CASCADE, default="", blank=True)
    id_salon = models.ForeignKey(Salon, on_delete=models.CASCADE, default="", blank=True)
    grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE, default="", blank=True)
    bdcontratista=models.ForeignKey(BDcontratista, on_delete=models.CASCADE, default="", blank=True)
    Rsala=models.BooleanField(default=False)
    observacion=models.CharField(max_length=300, blank=True,default="",null=True)
    Cupo=models.IntegerField(null=True, blank=True)
    CupoG=models.IntegerField(null=True, blank=True)
    CupoPostM=models.IntegerField(null=True, blank=True)

class Cprogramacion(models.Model):
     id=models.AutoField(primary_key=True)
     programacion=models.ManyToManyField(Programacion, related_name='cprogramacion')

class itinerario(models.Model):
    id=models.AutoField(primary_key=True)
    programa=models.ForeignKey(Programas, on_delete=models.CASCADE, default="", blank=True)
    cprogramacion = models.ForeignKey(Cprogramacion, on_delete=models.CASCADE, default=None, blank=True, related_name='programaciones')
    activo = models.BooleanField(default=True)

class Tapoyoxprograma(models.Model):
    id=models.AutoField(primary_key=True)
    Tapoyo=models.ForeignKey(User, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programas, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = ['Tapoyo']
