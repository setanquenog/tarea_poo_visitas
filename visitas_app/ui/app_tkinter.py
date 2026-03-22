# ============================
# Archivo: ui/app_tkinter.py
# ============================

import tkinter as tk
from tkinter import ttk, messagebox

class AppTkinter:
    """
    Clase de la interfaz gráfica.
    Recibe el servicio por dependencias.
    """

    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("700x500")


        # ======================
        # FORMULARIO
        # ======================
        # Se alinean etiquetas a la izquierda y pegadas a los Entry
        frame_form = tk.Frame(root)
        frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        tk.Label(frame_form, text="Cédula:", anchor="w", width=12).grid(row=0, column=0, padx=2, pady=5, sticky="w")
        self.entry_cedula = tk.Entry(frame_form, width=30)
        self.entry_cedula.grid(row=0, column=1, padx=2, pady=5, sticky="w")

        tk.Label(frame_form, text="Nombre:", anchor="w", width=12).grid(row=1, column=0, padx=2, pady=5, sticky="w")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=2, pady=5, sticky="w")

        tk.Label(frame_form, text="Motivo:", anchor="w", width=12).grid(row=2, column=0, padx=2, pady=5, sticky="w")
        self.entry_motivo = tk.Entry(frame_form, width=30)
        self.entry_motivo.grid(row=2, column=1, padx=2, pady=5, sticky="w")

        # ======================
        # BOTONES
        # ======================
        frame_botones = tk.Frame(root)
        frame_botones.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Botón Registrar (verde)
        tk.Button(frame_botones, text="Registrar", bg="green", fg="white",
                  width=12, command=self.registrar).grid(row=0, column=0, padx=5)

        # Botón Visualizar (verde)
        tk.Button(frame_botones, text="Visualizar", bg="green", fg="white",
                  width=12, command=self.actualizar_tabla).grid(row=0, column=1, padx=5)
        # Botón Limpiar (verde)
        tk.Button(frame_botones, text="Limpiar", bg="green", fg="white",
                  width=12, command=self.limpiar_campos).grid(row=0, column=2, padx=5)

        # Botón Eliminar (rojo)
        tk.Button(frame_botones, text="Eliminar", bg="red", fg="white",
                  width=12, command=self.eliminar).grid(row=0, column=3, padx=5)

        # ======================
        # TABLA
        # ======================
        self.tree = ttk.Treeview(root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def registrar(self):
        """
        Obtiene datos del formulario y registra un visitante.
        """
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        # Validación
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        from modelos.visitante import Visitante

        visitante = Visitante(cedula, nombre, motivo)

        if self.servicio.registrar_visitante(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar_tabla(self):
        """
        Actualiza la tabla con los datos actuales.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.obtener_visitantes():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def eliminar(self):
        """
        Elimina el visitante seleccionado.
        """
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        valores = self.tree.item(seleccionado, "values")
        cedula = valores[0]

        if self.servicio.eliminar_visitante(cedula):
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def limpiar_campos(self):
        """
        Limpia los campos del formulario.
        """
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)