from abc import ABC, abstractmethod
from enums import EstadoVehiculo
from excepciones import TarifaInvalidaError

class Vehiculo(ABC):
    def __init__(self, patente, marca, modelo, tarifa_base):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.tarifa_base = tarifa_base
        self._estado = EstadoVehiculo.DISPONIBLE

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if valor <= 0:
            raise TarifaInvalidaError("La tarifa base tiene que ser mayor a cero.")
        self._tarifa_base = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if not isinstance(nuevo_estado, EstadoVehiculo):
            raise ValueError("Estado invalido.")
        self._estado = nuevo_estado

    def esta_disponible(self):
        return self._estado == EstadoVehiculo.DISPONIBLE

    @abstractmethod
    def calcular_costo(self, dias):
        pass

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente}) - {self._estado.value}"


class Auto(Vehiculo):
    def calcular_costo(self, dias):
        return self.tarifa_base * dias


class Camioneta(Vehiculo):
    def calcular_costo(self, dias):
        return self.tarifa_base * 1.20 * dias


class Moto(Vehiculo):
    def calcular_costo(self, dias):
        return self.tarifa_base * 0.85 * dias