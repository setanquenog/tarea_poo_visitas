# Ejecución del programa Sistema de Registros de Visitantes
### Para ejecutar el programa se debe tener instalado Python 3.x, no se rerquiere de librerías externas, usando la libreía tkinter que ya viene con Python.
## Estructura del Proyecto

```
visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py
```
## Ejecutar la aplicación
1. Abrir la consola o terminal
2. Navegar hasta la carpeta del proyecto visitas_app
3. En main.py ejecutar el archivo principal
## Uso del sistema 
- Ingresar los datos del visitante en el formulario: . Cédula  . Nombre . Motivo.
- Presionar **Registrar**  para guardar la información.
- Presionar **Visualizar** para actualizar la tabla.
- Seleccionar un registro y presionar **Eliminar** para borrarlo.
- Presionar **Limpiar** para vaciar los campos.
## Detalle
### El sistema valida que no existan cédulas duplicadas. 
