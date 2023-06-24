from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Asignaturas, Programas, Proyeccion, TipoJornada, Cproyeccion, Mensajes, Casignatura, Dia, Disponibilidad, HorarioProfesor, HorarioDia,Rango, MensajesDisponibilidad, Salon, Tiposalon,Programacion,Cronograma,Ccronograma,Bitacora,Grupo,BDcontratista,itinerario,Tapoyoxprograma
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'groups','cedula']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Correo'}),
            'password1': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-sm', 'placeholder': 'Contraseña', 'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-sm', 'placeholder': 'Repita la contraseña', 'id': 'id_password2'}),
            'groups': forms.SelectMultiple(choices=Group.objects.all().values_list('name', 'name'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Roles'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Cedula'})
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','cedula']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Correo'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Cedula'})
        }


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignaturas
        fields = ['codigo', 'nombre', 'creditos',
                  'intensidad', 'semestre', 'programa']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Codigo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre Asignatura'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Semestre'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Creditos'}),
            'intensidad': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Intensidad'}),
            'programa': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Seleccione un programa'}),
        }


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programas
        fields = ['codigo', 'nombre', 'correo', 'username', 'jornada']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Codigo'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre del programa'}),
            'correo': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Correo del programa'}),
            'username': forms.Select(choices=User.objects.all().values_list('username', 'username'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor de apoyo'}),
            'jornada': forms.Select(choices=TipoJornada.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Jornada'}),

        }


class ProyeccionForm(forms.ModelForm):
    class Meta:
        model = Proyeccion
        fields = ['semestre', 'programas', 'activo']
        widgets = {
            'programas': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Programas'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Semestre'}),
        }
        activo = forms.BooleanField(
            widget=forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': '#Habilitado',
                'type': 'checkbox',
                'value': 'Valor del campo'
            }))


class CasignaturaForm(forms.ModelForm):
    class Meta:
        model = Casignatura
        fields = ['asignaturas', 'total_semanas', 'num_docentes']

        widgets = {
            'asignaturas': forms.Select(choices=Asignaturas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Asignatura'}),
            'total_semanas': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Semanas'}),
            'num_docentes': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Docentes'}),

        }


class CproyeccionForm(forms.ModelForm):
    class Meta:
        model = Cproyeccion
        fields = ['Casignatura']


class TareaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['usuario_emisor'].choices = User.objects.exclude(
            username=user.username).values_list('id', 'username')

    class Meta:
        model = Mensajes
        fields = ['mensaje', 'usuario_emisor', 'proyeccion']

        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3, 'placeholder': 'Descripción de la tarea', 'placeholder': 'Mensaje'}),
            'usuario_emisor': forms.Select(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
            'proyeccion': forms.Select(choices=Proyeccion.objects.all().values_list('id', 'programas'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
        }


class TareadisponForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['usuario_emisor'].choices = User.objects.exclude(
            username=user.username).values_list('id', 'username')

    class Meta:
        model = MensajesDisponibilidad
        fields = ['mensaje', 'usuario_emisor', 'disponibilidad']

        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3, 'placeholder': 'Descripción de la tarea', 'placeholder': 'Mensaje'}),
            'usuario_emisor': forms.Select(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
            'disponibilidad': forms.Select(choices=Disponibilidad.objects.all().values_list('id', 'Profesor'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
        }


class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['Profesor']

        widgets = {
            'Profesor': forms.Select(choices=Disponibilidad.objects.all().values_list('Profesor', 'Profesor'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor'}),
        }

    def clean(self):
        cleaned_data = super(DisponibilidadForm, self).clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError(
                    'La fecha de fin debe ser posterior a la fecha de inicio')
        return cleaned_data


class HorarioProfesorForm(forms.ModelForm):
    class Meta:
        model = HorarioProfesor
        fields = ['cdia']
        
        def clean(self):
            cleaned_data = super().clean()
            cdia = cleaned_data.get('cdia')

            if cdia and cdia.filter(dia=cdia.dia).exists():
                raise forms.ValidationError("Ya existe un cdia con el mismo día en esta Cdisponibilidad.")


class HorarioDiaForm(forms.ModelForm):
    class Meta:
        model = HorarioDia
        fields = ['dia', 'a', 'b', 'c', 'd', 'e']

        widgets = {
            'dia': forms.Select(choices=Dia.objects.all().values_list('Nombre', 'Nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Dia'}),
            'a': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'b': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'c': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'd': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'e': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class RangoForm(forms.ModelForm):
    class Meta:
        model = Rango
        fields = ['fecha_inicio', 'fecha_limite']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'datepicker', 'id': "date"}),
            'fecha_limite': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'datepicker', 'id': "date"}),

        }

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['nombre', 'tipo', 'capacidad']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'rows': 3, 'placeholder': 'Nombre del salon'}),
            'tipo': forms.Select(choices=Tiposalon.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'tipo'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Capacidad'})
        }


class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ['id_asignaturas','id_authuser', 'id_salon', 'Rsala','observacion','Cupo','CupoG','CupoPostM', 'grupo',
    'bdcontratista']

        widgets = {

            'id_asignaturas': forms.Select(choices=Asignaturas.objects.all().values_list('id', 'nombre'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Asignatura'}),
            'id_authuser': forms.Select(choices=User.objects.all().values_list('id', 'first_name'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Profesor','id':'select1'}),
            'id_salon': forms.Select(choices=Salon.objects.all().values_list('id', 'nombre'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Salon'}),
            'grupo': forms.Select(choices=Grupo.objects.all().values_list('id', 'nombre'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Grupo'}),
    'bdcontratista':forms.Select(choices=BDcontratista.objects.all().values_list('id', 'nombre'), attrs={'class': ' selectpicker form-control form-control-sm', 'placeholder': '¿Profesor elegible?'}),
            'observacion':forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3, 'placeholder': 'Descripción de la tarea', 'placeholder': 'Observacion'}),
            'Cupo':forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Cupo'}),
            'CupoG':forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Cupos Genericos'}),
            'CupoPostM':forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Cupos Post-Matricula'})
        }

class itinerarioForm(forms.ModelForm):
    class Meta:
        model = itinerario
        fields = ['programa']
        widgets = {
            'programa': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Programas'}),    
            }

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = ['programa','Profesor','asignatura']
        widgets = {
            'programa': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Programas'}),
            'Profesor': forms.Select(choices=User.objects.all().values_list('username', 'username'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor'}),
            'asignatura': forms.Select(choices=Asignaturas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Asisgnatura'}),
        }
                
class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['semana','fecha','Tema', 'material']
        widgets = {
            'semana': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Semana'}),
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'datepicker','id': "Fecha"}),
            'Tema': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Tema'}),
            'material': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Material'}),
        }

class BitacoraEditForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['Tema', 'material']
        widgets = {
            'semana': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '#Semana'}),
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'datepicker','id': "Fecha"}),
            'Tema': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Tema'}),
            'material': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Material'}),
        }        
       
class TapoyoxProgramaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TapoyoxProgramaForm, self).__init__(*args, **kwargs)
        self.fields['Tapoyo'].queryset = User.objects.filter(groups__name='Técnico de apoyo')

    class Meta:
        model = Tapoyoxprograma
        fields = ['Tapoyo', 'programa']
        widgets = {
            'Tapoyo': forms.Select(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Técnico de apoyo'}),
            'programa': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Programas'}),
        }