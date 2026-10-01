class Sucursal:
    def __init__(self, codigo, ciudad, direccion):
        self.codigo = codigo
        self.ciudad = ciudad
        self.direccion = direccion
        self._vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def quitar_vehiculo(self, vehiculo):
        self._vehiculos.remove(vehiculo)

    def listar_disponibles(self):
        return [v for v in self._vehiculos if v.esta_disponible()]

    def __str__(self):
        return f"Sucursal {self.codigo} - {self.ciudad} ({self.direccion})"