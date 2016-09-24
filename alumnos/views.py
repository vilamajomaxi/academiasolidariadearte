from django.shortcuts import render, redirect
# Create your views here.
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from alumnos.forms import LoginForm, AlumnoForm,Filter_form
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from alumnos.models import Alumno,Asistencia,Clase
from django.utils import timezone
from django.shortcuts import render, redirect




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/dash')
            else:
                pass
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})




@login_required
def agregar_alumno(request):
    try:
        coordinador = User.objects.get(username=request.user)
    except ObjectDoesNotExist:
        raise Http404("Usuario no existente")
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dash/')
        else:
            render(request, 'agregar_alumno.html', {'form': form})
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})


@login_required
def reporte(request):
    alumnos = Alumno.objects.all()
    for alumno in alumnos:
        asistencias = Asistencia.objects.filter(alumno = alumno)
        alumno.consolidacion = asistencias.filter(clase__tipo='CV').count()
        alumno.clase =  asistencias.filter(clase__tipo='R').count()
        alumno.devolucion = asistencias.filter(clase__tipo='DS').count()
    return render(request,'dash.html',{'alumnos':alumnos})



def filter(request):
    if request.method == 'POST':
        form = Filter_form(request.POST)
        if form.is_valid():
            mes = form.cleaned_data['mes']
            sede = form.cleaned_data['sede']
            alumnos = Alumno.objects.all()
            if sede:
                alumnos = alumnos.filter(sede = sede)
            for alumno in alumnos:
                if mes:
                    asistencias = Asistencia.objects.filter(alumno=alumno, fecha_hora__month=int(mes) + 1)
                else:
                    asistencias = Asistencia.objects.filter(alumno=alumno)
                asistencias = Asistencia.objects.filter(alumno = alumno)
                alumno.consolidacion = asistencias.filter(clase__tipo='CV').count()
                alumno.clase =  asistencias.filter(clase__tipo='R').count()
                alumno.devolucion = asistencias.filter(clase__tipo='DS').count()



            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/dash')
            else:
                pass
    else:
        form=Filter_form()
    return render(request,'filter.html',{'form':form})
