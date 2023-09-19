from django.shortcuts import render
from .models import Candidato, Elecciones


c = Elecciones()


def formulario(request):
    return render(request, "formulario.html")


def inscripcion(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    mensaje = c.inscribir(nombre, apellido)
    return render(request, "inscripcion.html", context={"mensaje": mensaje})


def votar(request):
    candidatos = c.candidatos

    return render(request, "votar.html", {"candidatos": candidatos})


def resultados(request):
    mensaje = c.resultados()
    return render(request, "resultados.html", context={"mensaje": mensaje})


def registro(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    mensaje = c.votar(nombre, apellido)
    return render(request, "registro.html", context={"mensaje": mensaje})
