from datetime import date, timedelta
from cliente import Cliente
from vehiculo import Auto, Camioneta, Moto
from sucursal import Sucursal
from reserva import Reserva
from notificador import ServicioNotificaciones
from excepciones import TarifaInvalidaError, FechaInvalidaError, VehiculoNoDisponibleError, TransicionEstadoInvalidaError
from enums import EstadoVehiculo, EstadoReserva

def main():
    print("=== SISTEMA DE ALQUILER DE VEHICULOS ===\n")

    cliente = Cliente("Inti", "Echeverria", "30111222", "2994567890", "inti@mail.com")
    print("Cliente creado:", cliente)

    auto = Auto("ABC123", "Toyota", "Corolla", 150000)
    camioneta = Camioneta("DEF456", "Ford", "Ranger", 200000)
    moto = Moto("GHI789", "Mondial", "ZB110", 80000)
    print("\nVehiculos creados:")
    print(" ", auto)
    print(" ", camioneta)
    print(" ", moto)

    sucursal = Sucursal("S01", "Cutral-co", "Av. Roca 123")
    sucursal.agregar_vehiculo(auto)
    sucursal.agregar_vehiculo(camioneta)
    sucursal.agregar_vehiculo(moto)
    print("\n", sucursal)
    print("Vehiculos disponibles:", len(sucursal.listar_disponibles()))

    
    hoy = date.today()
    reserva = Reserva(cliente, auto, hoy, hoy + timedelta(days=5))
    print("\nReserva creada:", reserva)
    print("Costo del alquiler:", reserva.calcular_costo())

    
    print("Costo Auto (5 dias):", auto.calcular_costo(5))
    print("Costo Camioneta (5 dias):", camioneta.calcular_costo(5))
    print("Costo Moto (5 dias):", moto.calcular_costo(5))

    
    reserva.confirmar()
    reserva.iniciar()
    reserva.finalizar()
    print("Historial de reserva:")
    for r in reserva.historial:
        print(" ", r)

    
    notificador = ServicioNotificaciones()
    notificador.notificar(cliente, "Tu alquiler ha finalizado")

    

    try:
        Auto("ZZZ000", "Fiat", "Palio", -100)
    except TarifaInvalidaError as e:
        print("Error 1 - Tarifa invalida:", e)

    try:
        Reserva(cliente, camioneta, hoy, hoy - timedelta(days=1))
    except FechaInvalidaError as e:
        print("Error 2 - Fecha invalida:", e)

    try:
        moto.estado = EstadoVehiculo.FUERA_DE_SERVICIO
        r2 = Reserva(cliente, moto, hoy, hoy + timedelta(days=2))
        r2.confirmar()
    except VehiculoNoDisponibleError as e:
        print("Error 3 - Vehiculo no disponible:", e)

    try:
        r3 = Reserva(cliente, auto, hoy, hoy + timedelta(days=3))
        r3._cambiar_estado(EstadoReserva.FINALIZADA, "Salto invalido")
    except TransicionEstadoInvalidaError as e:
        print("Error 4 - Transicion invalida:", e)

if __name__ == "__main__":
    main()