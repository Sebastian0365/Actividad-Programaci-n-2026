# Esta clase representa a un cliente del sistema
class Cliente:

    # Constructor con validaciones
    def __init__(self, nombre, edad):
        # Validamos que el nombre no esté vacío
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        # Validamos que la edad sea válida
        if edad <= 0:
            raise ValueError("Edad inválida")

        # Guardamos los datos del cliente
        self.nombre = nombre
        self.edad = edad

    # Método para mostrar la información del cliente
    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}"