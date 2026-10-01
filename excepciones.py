
class TarifaInvalidaError(ValueError):
    """Se lanza cuando la tarifa base es menor o igual a cero."""
    pass

class FechaInvalidaError(ValueError):
    """Se lanza cuando la fecha de fin es anterior a la de inicio."""
    pass

class VehiculoNoDisponibleError(Exception):
    """Se lanza cuando se intenta confirmar una reserva con un vehiculo no disponible."""
    pass

class TransicionEstadoInvalidaError(Exception):
    """Se lanza cuando se intenta hacer un cambio de estado no permitido."""
    pass