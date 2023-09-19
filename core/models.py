from django.db import models


class Candidato:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.votos = 0


class Elecciones:
    def __init__(self) -> None:
        self.candidatos = []

    def inscribir(self, nombre, apellido):
        nuevo_candidato = Candidato(nombre, apellido)
        self.candidatos.append(nuevo_candidato)
        return "Candidato Inscrito con Exito"

    def votar(self, nombre, apellido):
        for candidato in self.candidatos:
            if nombre == candidato.nombre and apellido == candidato.apellido:
                candidato.votos += 1
                return "Voto Agregado con Exito"
        return "Candidato no encontrado"

    def resultados(self):
        if not self.candidatos:
            return "No hay candidatos"
        ganador = max(self.candidatos, key=lambda candidato: candidato.votos)
        return ganador
