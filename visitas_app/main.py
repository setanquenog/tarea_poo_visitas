# ============================
# Archivo: main.py
# ============================

import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    # Crear servicio (lógica de negocio)
    servicio = VisitaServicio()

    # Crear ventana principal
    root = tk.Tk()

    # Inyección de dependencias (pasamos el servicio a la UI)
    app = AppTkinter(root, servicio)

    # Ejecutar aplicación
    root.mainloop()