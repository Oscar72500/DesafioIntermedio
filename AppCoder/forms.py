from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) 
    comision = forms.IntegerField()
    numero_dia = forms.IntegerField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) 
    comision = forms.IntegerField()
    cantidad_dia = forms.IntegerField()

class MateriasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40) 
    comision = forms.IntegerField()
    cantidad_dia = forms.IntegerField()    