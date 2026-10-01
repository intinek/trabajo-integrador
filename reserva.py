from enums import EstadoReserva, EstadoVehiculo
from excepciones import FechaInvalidaError, VehiculoNoDisponibleError, TransicionEstadoInvalidaError
from historial import RegistroHistorial

class Reserva:
    _contador = 0

    def __init__(self, cliente, vehiculo, fecha_inicio, fecha_fin):
        if fecha_fin <= fecha_inicio:
            raise FechaInvalidaError("La fecha de fin debe ser posterior a la de inicio.")

        Reserva._contador += 1
        self.numero = Reserva._contador
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self._estado = EstadoReserva.SOLICITADA
        self._historial = []
        self._historial.append(RegistroHistorial(self._estado, "Reserva creada."))

    @property
    def estado(self):
        return self._estado

    def _cambiar_estado(self, nuevo_estado, descripcion):
        self._validar_transicion(nuevo_estado)
        self._estado = nuevo_estado
        self._historial.append(RegistroHistorial(nuevo_estado, descripcion))

    def _validar_transicion(self, nuevo_estado):
        if self._estado == EstadoReserva.SOLICITADA and nuevo_estado == EstadoReserva.FINALIZADA:
            raise TransicionEstadoInvalidaError(
                "Una reserva SOLICITADA no puede pasar directamente a FINALIZADA."
            )

    def confirmar(self):
        if not self.vehiculo.esta_disponible():
            raise VehiculoNoDisponibleError(
                f"El vehiculo {self.vehiculo.patente} no esta disponible."
            )
        self._cambiar_estado(EstadoReserva.CONFIRMADA, "Reserva confirmada.")
        self.vehiculo.estado = EstadoVehiculo.RESERVADO

    def iniciar(self):
        self._cambiar_estado(EstadoReserva.EN_CURSO, "Alquiler iniciado.")
        self.vehiculo.estado = EstadoVehiculo.EN_ALQUILER

    def finalizar(self):
        self._cambiar_estado(EstadoReserva.FINALIZADA, "Alquiler finalizado.")
        self.vehiculo.estado = EstadoVehiculo.DISPONIBLE

    def cancelar(self):
        self._cambiar_estado(EstadoReserva.CANCELADA, "Reserva cancelada.")
        if self.vehiculo.estado == EstadoVehiculo.RESERVADO:
            self.vehiculo.estado = EstadoVehiculo.DISPONIBLE

    def calcular_costo(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        if dias <= 0:
            raise FechaInvalidaError("La reserva debe durar al menos un dia.")
        return self.vehiculo.calcular_costo(dias)

    @property
    def historial(self):
        return list(self._historial)

    def __str__(self):
        return f"Reserva #{self.numero} | {self.cliente} | {self.vehiculo.patente} | {self._estado.value}"