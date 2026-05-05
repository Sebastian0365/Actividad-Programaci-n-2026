from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva


#caso correcto
try:
    cliente1 = Cliente("Gaby", 19)
    servicio1 = ReservaSala("sala VIP") 
    reserva1 = Reserva(cliente1, servicio1, 2)

    print(reserva1.mostrar())
    print("costo:", reserva1.calcular_total())

except Exception as e:
    print("error:", e)
    
    
#caso con error
try:
    cliente2 = Cliente("", -5)  #datos inválidos
    
except Exception as e:
    print("error detectado:", e)


#otro servicio
try:
    servicio2 = AlquilerEquipo("equipo sonido")
    reserva2 = Reserva(cliente1, servicio2, 3)

    print(reserva2.mostrar())
    print("costo:", reserva2.calcular_total())

except Exception as e:
    print("error:", e)