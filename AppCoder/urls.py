from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursosApi/', views.cursosapi),
    path('cursosApi/', views.cursosapi),
    path('profesoresApi/', views.profesoresapi),
    path('materiasApi/', views.materiasapi),
    path('profesores/', views.profesores, name='profesores'),
    path('materias/', views.materias, name='materias'),
    path('busquedaCurso', views.busquedaCurso, name="busquedaCurso"),
    path('busquedaProfesores', views.busquedaProfesores, name="busquedaProfesores"),
    path('busquedaMaterias', views.busquedaMaterias, name="busquedaMaterias"),
    path('buscar/', views.buscar),
    path('buscarprofesor/', views.buscarprofesor),
    path('buscarmaterias/', views.buscarmateria)
]
