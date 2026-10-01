class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"