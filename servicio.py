# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    # Método que deben implementar las clases hijas
    @abstractmethod
    def calcular_costo(self):
        pass


# Clase que representa el servicio de reserva de salas
class ReservaSala(Servicio):

    # Método para calcular el costo según las horas
    def calcular_costo(self, horas):
        # Validamos que las horas sean correctas
        if horas <= 0:
            raise ValueError("Horas inválidas")

        # Retornamos el costo total
        return horas * 50000