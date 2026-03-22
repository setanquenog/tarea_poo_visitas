# ============================
# Archivo: servicios/visita_servicio.py
# ============================

class VisitaServicio:
    """
    Clase encargada de la lógica de negocio (CRUD).
    Gestiona internamente la lista de visitantes.
    """

    def __init__(self):
        # Lista privada para almacenar visitantes
        self._visitantes = []

    def registrar_visitante(self, visitante):
        """
        Registra un nuevo visitante si la cédula no existe.
        """
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False  # Ya existe

        self._visitantes.append(visitante)
        return True

    def obtener_visitantes(self):
        """
        Retorna la lista de visitantes.
        """
        return self._visitantes

    def eliminar_visitante(self, cedula):
        """
        Elimina un visitante por su cédula.
        """
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False