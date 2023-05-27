from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Asignaturas, Programas, Proyeccion, TipoJornada, Cproyeccion, Mensajes, Casignatura, Dia, Disponibilidad, Cdisponibilidad, Cdia, asignaturaXprofesor, calendario, casigXprofe, Rango, MensajesDisponibilidad, Salon, Tiposalon,Programacion
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'groups']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Correo'}),
            'password1': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-sm', 'placeholder': 'Contraseña', 'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control form-control-sm', 'placeholder': 'Repita la contraseña', 'id': 'id_password2'}),
            'groups': forms.SelectMultiple(choices=Group.objects.all().values_list('name', 'name'), attrs={'class': 'selectpicker form-control form-control-sm', 'placeholder': 'Roles'}),
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Correo'}),
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
            'proyeccion': forms.Select(choices=Proyeccion.objects.all().values_list('programas', 'programas'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
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
            'disponibilidad': forms.Select(choices=Disponibilidad.objects.all().values_list('Profesor', 'Profesor'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Proyeccion'}),
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


class CdsponibilidadForm(forms.ModelForm):
    class Meta:
        model = Cdisponibilidad
        fields = ['cdia']
        
        def clean(self):
            cleaned_data = super().clean()
            cdia = cleaned_data.get('cdia')

            if cdia and cdia.filter(dia=cdia.dia).exists():
                raise forms.ValidationError("Ya existe un cdia con el mismo día en esta Cdisponibilidad.")


class CdiaForm(forms.ModelForm):
    class Meta:
        model = Cdia
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


class AsignaturaXProfesorForm(forms.ModelForm):
    class Meta:
        model = asignaturaXprofesor
        fields = ['Profesor', 'Asignatura']

        widgets = {
            'Profesor': forms.Select(choices=User.objects.all().values_list('username', 'username'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor'}),
            'Asignatura': forms.Select(choices=Asignaturas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Asignatura'}),
        }


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = calendario
        fields = ['Programa']

    def clean(self):
        cleaned_data = super().clean()
        programa = cleaned_data.get("Programa")

        if calendario.objects.filter(Programa=programa).exists():
            raise forms.ValidationError(
                "Ya existe un calendario para este programa.")


class CasigXprofeForm(forms.ModelForm):
    class Meta:
        model = casigXprofe
        fields = ['asigXprofe', 'dia', 'hora_inicioClase', 'hora_finClase']
        widgets = {
            'asigXprofe': forms.Select(choices=casigXprofe.objects.all().values_list('asigXprofe', 'asigXprofe'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor'}),
            'dia': forms.Select(choices=Dia.objects.all().values_list('Nombre', 'Nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Dia'}),
            'hora_inicioClase': forms.TimeInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-sm', 'placeholder': 'Hora inicio', 'id': "date"}),
            'hora_finClase': forms.TimeInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-sm', 'placeholder': 'Hora Fin', 'id': "date"}),
        }


class CasigXprofeForm(forms.ModelForm):
    class Meta:
        model = casigXprofe
        fields = ['asigXprofe', 'dia', 'hora_inicioClase', 'hora_finClase']

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicioClase')
        hora_fin = cleaned_data.get('hora_finClase')


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
        fields = ['id_asignaturas', 'id_programas',
                  'id_authuser', 'id_salon', 'hora', 'dia']

        widgets = {

            'id_asignaturas': forms.Select(choices=Asignaturas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Asignatura'}),
            'id_programas': forms.Select(choices=Programas.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Programas'}),
            'id_authuser': forms.Select(choices=User.objects.all().values_list('first_name', 'first_name'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profesor'}),
            'id_salon': forms.Select(choices=Salon.objects.all().values_list('nombre', 'nombre'), attrs={'class': 'form-control form-control-sm', 'placeholder': 'Salon'}),
            'hora': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'rows': 3, 'placeholder': 'Nombre del salon'}),
            'dia': forms.Select(choices=Dia.objects.all().values_list('Nombre', 'Nombre'),attrs={'class': 'form-control form-control-sm', 'placeholder': 'Capacidad'})
        }
