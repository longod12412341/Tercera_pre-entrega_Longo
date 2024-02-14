from django.shortcuts import render
from django.http import HttpResponse
from app_g.models import Curso

# Create your views here.

def inicio(request):
    return render(request, "index.html")
def cursos(request):
    cursos= Curso.objects.all()
    print(cursos)
    return render(request, "cursos.html", {"cursos":cursos})
def profesores(request):
    return render(request, "profesores.html")
def estudiantes(request):
    return render(request, "estudiantes.html")
def entregables(request):
    return render(request, "entregables.html")
