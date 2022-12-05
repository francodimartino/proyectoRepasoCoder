from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(request):

    
    curso1=Curso(nombre="js",comision=34645)
    curso1.save()
    curso2=Curso(nombre="Django",comision=321231)
    curso2.save()
    lista_cursos=[curso1, curso2]
    
    cadena_Texto="Curso guardado: "+curso1.nombre+" "+str(curso1.comision)

    return render(request,"AppCoder/curso.html", {"cursos":lista_cursos})
    return HttpResponse(cadena_Texto)