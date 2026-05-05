# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    # Método que deben implementar las clases hijas
    #agregamos parametro para que coincida con las clase hija
    @abstractmethod
    def calcular_costo(self, tiempo):
        pass


# Clase que representa el servicio de reserva de salas
class ReservaSala(Servicio):

    # Método para calcular el costo según las horas
    def calcular_costo(self, horas):
        # Validamos que las horas sean correctas
        if horas <= 0:
            raise ValueError("Horas inválidas")
        
        #validamos tipo de dato
        if not isinstance(horas, (int, float)):
            raise ValueError("Las horas deben ser numéricas")

        # Retornamos el costo total
        return horas * 50000
    


#clase que representa el servicio de alquiler de equipos
class AlquilerEquipo(Servicio):
    
    #metodo para calcular el costo segun los dias
    def calcular_costo(self, dias):
        #validamos que los días sean correctos
        if dias <= 0:
            raise ValueError("Días inválidos")
        
        #validamos tipo de dato
        if not isinstance(dias, (int, float)):
            raise ValueError("Los días deben ser numéricos")

        # Retornamos el costo total
        return dias * 30000


#clase que representa el servicio de asesoria
class Asesoria(Servicio):
    
    #metodo para calcular el costo segun las horas
    def calcular_costo(self, horas):
        #validamos que las horas sean correctas
        if horas <= 0:
            raise ValueError("Horas inválidas")
        
        #validamos tipo de dato
        if not isinstance(horas, (int, float)):
            raise ValueError("Las horas deben ser numéricas")

        # Retornamos el costo total
        return horas * 80000