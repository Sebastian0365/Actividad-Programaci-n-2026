from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_error, registrar_evento


#caso correcto
try:
    cliente1 = Cliente("Gaby", 19)
    servicio1 = ReservaSala("sala VIP") 
    reserva1 = Reserva(cliente1, servicio1, 2)

    print(reserva1.mostrar())
    print("costo:", reserva1.calcular_total())
    
    registrar_evento("Reserva de sala creada")

except Exception as e:
    print("error:", e)
    registrar_error(str(e))

finally:
    print("primer proceso finalizado")
    

#caso con error
try:
    cliente2 = Cliente("", -5)  #datos inválidos
    
except Exception as e:
    print("error detectado:", e)
    registrar_error(str(e))

finally:
    print("segundo proceso finalizado")


#otro servicio
try:
    servicio2 = AlquilerEquipo("equipo sonido")
    reserva2 = Reserva(cliente1, servicio2, 3)

    print(reserva2.mostrar())
    print("costo:", reserva2.calcular_total())
    
    registrar_evento("Reserva de equipo creada")

except Exception as e:
    print("error:", e)
    
finally:
    print("tercer proceso finalizado")
    


#servicio de asesoria
try:
    servicio3 = Asesoria("asesoria tecnica")
    reserva3 = Reserva(cliente1, servicio3, 4)

    print(reserva3.mostrar())
    print("costo:", reserva3.calcular_total())

    reserva3.confirmar()
    print("estado:", reserva3.estado)

    registrar_evento("Reserva de asesoria confirmada")

except Exception as e:
    print("error:", e)
    registrar_error(str(e))

finally:
    print("cuarto proceso finalizado")