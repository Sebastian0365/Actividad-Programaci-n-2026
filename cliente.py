# Esta clase representa a un cliente del sistema
class Cliente:

    # Constructor con validaciones
    def __init__(self, nombre, edad):
        #validamos que el nombre sea texto
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto")

        # Validamos que el nombre no esté vacío
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        # Validamos que la edad sea válida
        if edad <= 0:
            raise ValueError("Edad inválida")
        
        #validamos que la edad sea un numero
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero")
        
        #usamos encapsulación para proteger los atributos
        self.__nombre = nombre
        self.__edad = edad

    # Método para mostrar la información del cliente
    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}"
    
    # metodo para obtener nombre (buena practica)
    def get_nombre(self):
        return self.__nombre
    
    # compatibilidad con el resto del sistema
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad





