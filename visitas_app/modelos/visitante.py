# ============================
# Archivo: modelos/visitante.py
# ============================

class Visitante:
    """
    Clase modelo que representa a un visitante.
    Contiene únicamente datos (no lógica de negocio).
    """

    def __init__(self, cedula, nombre, motivo):
        # Atributos del visitante
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo