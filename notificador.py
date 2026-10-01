class ServicioNotificaciones:
    def notificar(self, cliente, mensaje):
        print(f"[NOTIFICACION a {cliente.email}] {mensaje}")