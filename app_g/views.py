from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "index.html")
def cursos(request):
    return render(request, "cursos.html")
def profesores(request):
    return render(request, "cursos.html")
def estudiantes(request):
    return render(request, "cursos.html")
def entregables(request):
    return render(request, "cursos.html")
