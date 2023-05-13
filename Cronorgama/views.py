from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, UserEditForm, AsignaturaForm, ProgramaForm, ProyeccionForm, CproyeccionForm, CasignaturaForm, DisponibilidadForm, CdiaForm
from .models import User, Asignaturas, Programas, Proyeccion, TipoJornada, Cproyeccion, Mensajes, Casignatura, Disponibilidad, Cdisponibilidad, Cdia
from django.contrib.auth.models import Group
import openpyxl
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.forms import formset_factory
from django.http import HttpResponse
from reportlab.lib.units import inch
from django.core.exceptions import ValidationError


# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


@login_required
def home(request):
    return render(request, 'Cronorgama/home.html')


@login_required
def desactivar(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect('table')


@login_required
def table(request):
    C_users = User.objects.all()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            selected_groups = request.POST.getlist('groups')
            groups = Group.objects.filter(id__in=selected_groups)

            for group in groups:
                group.user_set.add(user)
            return redirect('table')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Cronorgama/tables.html', {'form': form, 'C_users': C_users})


@login_required
def register(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('register')
    return render(request, 'Cronorgama/register.html')

@login_required
def exit(request):
    logout(request)
    return redirect('home')

@login_required
def load_users(request):
    C_users = User.objects.all()
    groups = Group.objects.all()
    if request.method == 'POST' and request.FILES['usuarios']:
        # Obtener el archivo del formulario
        file = request.FILES['usuarios']
        # Abrir el archivo con openpyxl
        workbook = openpyxl.load_workbook(file)
        # Seleccionar la hoja que contiene los datos de usuario
        sheet = workbook['Hoja1']
        # Iterar sobre cada fila de la hoja y guardar los datos en la base de datos
        for row in sheet.iter_rows(min_row=2, values_only=True):
            username, email, password, first_name, last_name, group_name = row
            password = str(password)  # Convertir la contraseña en una cadena
            user, created = User.objects.get_or_create(
                username=username, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.save()

            group, created = Group.objects.get_or_create(name=group_name)
            # Agregar al usuario al grupo
            user.groups.add(group)
            # Redirigir a una página de éxito después de guardar los datos
        return render(request, 'Cronorgama/tables.html', {'C_users': C_users, 'groups': groups})
    else:
        # Renderizar el formulario para cargar el archivo si el método no es POST
        return render(request, 'Cronorgama/load_users.html', {'C_users': C_users, 'groups': groups})

@login_required
def asignatura(request):
    asignaturas = Asignaturas.objects.all()
    programas = Programas.objects.all()
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asignatura')
    else:
        form = AsignaturaForm()
    return render(request, 'registerasig.html', {'form': form, 'asignaturas': asignaturas, 'programas': programas})

@login_required
def programa(request):
    usuarios = User.objects.all()
    tjornada = TipoJornada.objects.all()
    programas = Programas.objects.all()
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programa')
    else:
        form = ProgramaForm()
    return render(request, 'registerprom.html', {'form': form, 'programas': programas, 'usuarios': usuarios, 'tjornada': tjornada})

@login_required
def CproyeccionU(request, id):
    proyeccion = Proyeccion.objects.get(id=id)
    cAsignatura = proyeccion.cproyeccion.Casignatura
    if request.method == 'POST':
        form = CasignaturaForm(request.POST)
        if form.is_valid():
            try:
                casignatura = form.save(commit=False)
                casignatura.save()
                cproyeccion = proyeccion.cproyeccion
                cproyeccion.Casignatura.add(casignatura)
                return redirect('CproyeccionU', id=id)
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CasignaturaForm()
    return render(request, 'Cproyeccion.html', {'form': form, 'proyeccion': proyeccion, 'cAsignatura': cAsignatura})

@login_required
def proyeccion(request):
    asignaturas = Asignaturas.objects.all()
    programas = Programas.objects.all()
    proyecciones = Proyeccion.objects.all()
    if request.method == 'POST':
        form = ProyeccionForm(request.POST)
        if form.is_valid():
            try:
                # Crear la instancia de Cproyeccion y guardarla
                cproyeccion = Cproyeccion.objects.create()
                cproyeccion.save()

                # Crear la instancia de Proyeccion y asignar la clave primaria de Cproyeccion a cproyeccion
                proyeccion = form.save(commit=False)
                proyeccion.cproyeccion = cproyeccion
                proyeccion.save()

                return redirect('proyeccion')
            except ValueError as error:
                return render(request, 'registerproy.html', {'form': form, 'error_message': str(error), 'proyecciones': proyecciones, 'asignaturas': asignaturas, 'programas': programas})
    else:
        form = ProyeccionForm()
    return render(request, 'registerproy.html', {'form': form, 'proyecciones': proyecciones, 'asignaturas': asignaturas, 'programas': programas})

@login_required
def generar(request, id):
    if request.method == 'POST':
        cproyeccion = Proyeccion.objects.get(pk=id)
        asignaturas = cproyeccion.cproyeccion.Casignatura.all()

        data = []
        for asignatura in asignaturas:
            row = [
                asignatura.asignaturas.semestre,
                asignatura.asignaturas.codigo,
                asignatura.asignaturas.nombre,
                asignatura.asignaturas.creditos,
                asignatura.asignaturas.intensidad,
                asignatura.total_semanas,
                asignatura.num_docentes,
            ]
            data.append(row)
        # Crea el archivo PDF
        PAGE_WIDTH = sum([1.2, 1.8, 1.6, 1.8, 1.2, 1.8,
                         1.8, 1.8, 1.8]) * inch + 1 * inch
        PAGE_HEIGHT = letter[0]
        page_size = (PAGE_WIDTH, PAGE_HEIGHT)
        doc = SimpleDocTemplate("proyeccion.pdf", pagesize=page_size)
        styles = getSampleStyleSheet()
        table_style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.red),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 1, colors.black)
        ])

        header = ['Semestre', 'Codigo', 'Asignatura',
                  'Creditos', 'Horas semanales', 'Semanas', 'Num Docentes']
        data.insert(0, header)
        table = Table(data)
        table.setStyle(table_style)
        elements = []
        elements.append(table)
        doc.build(elements)

        # Retorna el archivo PDF como respuesta
        with open("proyeccion.pdf", "rb") as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=proyeccion.pdf'
            return response
    else:
        return render(request, 'registerproy.html')

@login_required
def modificarprom(request, id):
    programa = Programas.objects.get(id=id)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('programa')
    else:
        form = ProgramaForm(instance=programa)
    return render(request, 'Cronorgama/modificarProm.html', {'form': form, 'programa': programa})

@login_required
def desactivarpro(request):
    proyecciones = Proyeccion.objects.all()
    for Cproyeccion in proyecciones:
        Cproyeccion.activo = False
        Cproyeccion.save()
    return redirect('Cproyeccion')

@login_required
def activarpro(request):
    proyecciones = Proyeccion.objects.all()
    for Cproyeccion in proyecciones:
        Cproyeccion.activo = True
        Cproyeccion.save()
    return redirect('Cproyeccion')

@login_required
def modificar(request, id):
    proyeccion = Proyeccion.objects.get(id=id)
    if request.method == 'POST':
        form = ProyeccionForm(request.POST, instance=proyeccion)
        if form.is_valid():
            form.save()
            return redirect('proyeccion')
    else:
        form = ProyeccionForm(instance=proyeccion)
    return render(request, 'Cronorgama/modificarProy.html', {'form': form, 'proyeccion': proyeccion})

@login_required
def modificarasig(request, id):
    asignatura = Asignaturas.objects.get(id=id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('asignatura')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'Cronorgama/modificarAsig.html', {'form': form, 'asignatura': asignatura})

@login_required
def modificarusu(request, id):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'Cronorgama/PerfilUsuario.html', {'form': form, 'user': user})


@login_required
def enviar_tarea(request):
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        proyeccion_id = request.POST.get('proyeccion')
        mensaje = request.POST.get('mensaje')
        confirmar = False
        usuario_emisor = request.user

        # Verificar si el usuario destinatario existe
        try:
            destinatario = User.objects.get(username=destinatario)
        except User.DoesNotExist:
            messages.error(request, 'El usuario destinatario no existe')
            return redirect('enviar_tarea')

        # Crear el mensaje
        mensaje = Mensajes.objects.create(
            mensaje=mensaje,
            confirmar=confirmar,
            usuario_emisor=usuario_emisor,
            proyeccion_id=proyeccion_id,
        )

        # Asociar el mensaje a los destinatarios
        mensaje.usuarios_destinatarios.add(destinatario)

        messages.success(request, 'Tarea enviada exitosamente')
        return redirect('enviar_tarea')

    else:
        usuarios = User.objects.exclude(username=request.user.username)
        proyecciones = Proyeccion.objects.all()
        return render(request, 'enviar_tarea.html', {'usuarios': usuarios, 'proyecciones': proyecciones})


@login_required
def confirmar_mensaje(request, mensaje_id):
    mensaje = Mensajes.objects.get(id=mensaje_id)
    mensaje.confirmar = True
    mensaje.save()
    messages.success(request, 'Mensaje confirmado exitosamente')
    return redirect('mensajes_recibidos')


@login_required
def mensajes_recibidos(request):
    mensajes = Mensajes.objects.filter(usuarios_destinatarios=request.user)
    return render(request, 'mensajes_recibidos.html', {'mensajes': mensajes})


@login_required
def disponibilidad(request):
    disponibilidades = Disponibilidad.objects.all()
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)
        if form.is_valid():
            try:
                cdisponibilidad = Cdisponibilidad.objects.create()
                cdisponibilidad.save()

                disponibilidad = form.save(commit=False)
                disponibilidad.cdisponibilidad = cdisponibilidad
                disponibilidad.save()

                return redirect('disponibilidad')
            except ValueError as error:
                return render(request, 'Cronorgama/Disponibilidad.html', {'form': form, 'error_message': str(error), 'disponibilidades': disponibilidades})
    else:
        form = DisponibilidadForm()
    return render(request, 'Cronorgama/Disponibilidad.html', {'form': form, 'disponibilidades': disponibilidades})

@login_required
def CdisponibilidadU(request, id):
    disponibilidad = Disponibilidad.objects.get(id=id)
    cdias = disponibilidad.cdisponibilidad.cdia
    if request.method == 'POST':
        form = CdiaForm(request.POST)
        if form.is_valid():
            try:
                cdia = form.save(commit=False)
                cdia.save()
                cdisponibilidad1 = disponibilidad.cdisponibilidad
                cdisponibilidad1.cdia.add(cdia)
                return redirect('CdisponibilidadU', id=id)
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CdiaForm()
    return render(request, 'Cronorgama/DisponibilidadXusuario.html', {'form': form, 'cdias': cdias})
