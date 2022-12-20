from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesores, Materias
from django.core import serializers

from AppCoder.forms import CursoFormulario, ProfesoresFormulario, MateriasFormulario



def busquedaCurso(request):
    return render(request, "AppCoder/busquedaCurso.html")

def busquedaProfesores(request):
    return render(request, "AppCoder/busquedaProfesores.html")

def busquedaMaterias(request):
    return render(request, "AppCoder/busquedaMaterias.html")

def buscar(request):
    
    comision_views = request.GET["comision"]
    curso_todos=Curso.objects.filter(comision=comision_views)
    
    return render(request,"AppCoder/ResultadoCurso.html",{"cursos":curso_todos, "comision":comision_views}) 
    
    #return HttpResponse(f"Buscando la camada {comision_views} que tiene la variable {curso_todos}")
    
    #if request.GET["camada"]:
        #camada = request.GET['camada']
        #cursos = Curso.objects.filter(camada=camada)
        #return render(request,"AppCoder/ResultadoCurso.html",{"cursos":cursos,"camada":camada})
    #else:
        #respuesta = "No enviaste datos"
    #return HttpResponse(respuesta)

def buscarprofesor(request):
    
    comision_views = request.GET["comision"]
    profesor_todos=Profesores.objects.filter(comision=comision_views)
    
    return render(request,"AppCoder/ResultadoProfesores.html",{"Profesores":profesor_todos, "comision":comision_views})

def buscarmateria(request):
    
    comision_views = request.GET["comision"]
    materias_todos=Materias.objects.filter(comision=comision_views)
    
    return render(request,"AppCoder/ResultadoMaterias.html",{"Materias":materias_todos, "comision":comision_views}) 
 


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(
                nombre=informacion["nombre"], comision=informacion["comision"], numero_dia=informacion["numero_dia"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


# def profesores(request):
 #   return HttpResponse('Vistas de Profesores')

def profesores(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = ProfesoresFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesores(
                nombre=informacion["nombre"], comision=informacion["comision"], cantidad_dia=informacion["cantidad_dia"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesoresFormulario()
    return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})


def materias(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = MateriasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            materia = Materias(
                nombre=informacion["nombre"], comision=informacion["comision"], cantidad_dia=informacion["cantidad_dia"])
            materia.save()
            return render(request, "AppCoder/materias.html")
    else:
        miFormulario = MateriasFormulario()
    return render(request, "AppCoder/materias.html", {"miFormulario": miFormulario})


def cursosapi(request):
    cursos_todos = Curso.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_todos))

def profesoresapi(request):
    cursos_todos = Profesores.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_todos))

def materiasapi(request):
    cursos_todos = Materias.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_todos))
