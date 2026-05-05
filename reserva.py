#importamos las clases necesarias
from cliente import Cliente
from servicio import Servicio

#clase reserva que conecta cliente y servicio
class Reserva:
    def __init__(self, cliente, servicio, tiempo):
        
        #validamos que sea un cliente
        if not isinstance(cliente, Cliente):
            raise ValueError("Cliente invalido")
        
        #validamos que sea un servicio
        if not isinstance(servicio, Servicio):
            raise ValueError("Servicio invalido")
        
        #validamos el tiempo
        if tiempo <= 0:
            raise ValueError("Tiempo invalido")
        
        
        #guardamos los datos
        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "Pendiente"
    
    
    #metodo para confirmar la reserva
    def confirmar(self):
        self.estado = "Confirmada"
        
    
    #metodo para cancelar la reserva
    def cancelar(self):
        self.estado = "Cancelada"
        
    #metodo para calcular el costo total
    def calcular_total(self):
        try:
            return self.servicio.calcular_costo(self.tiempo)
        except Exception as e:
            raise ValueError(f"error al calcular costo: {e}")
    
    #metodo para mostrar la información
    def mostrar(self):
        return f"{self.cliente.mostrar_info()} - servicio:{self.servicio.nombre} - tiempo:{self.tiempo} - estado:{self.estado}"