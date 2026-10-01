from datetime import datetime

class RegistroHistorial:
    def __init__(self, estado, descripcion):
        self.fecha_hora = datetime.now()
        self.estado = estado
        self.descripcion = descripcion

    def __str__(self):
        fecha = self.fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"[{fecha}] {self.estado.value} - {self.descripcion}"