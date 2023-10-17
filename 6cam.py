from tkinter import *
from tkinter import messagebox
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

# Función para capturar imágenes de una cámara en un hilo separado
def capture_camera(camera_id, canvas):
    cap = cv2.VideoCapture(camera_id)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)

        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.photo = photo

    cap.release()

# Función para abrir una ventana de configuración de cámara
def configure_camera():
    if len(cameras) >= 6:
        messagebox.showinfo("Advertencia", "No es posible agregar más cámaras.")
        return

    # Crear una ventana emergente para la configuración
    config_window = tk.Toplevel(root)
    config_window.title("Configurar Cámara")

    # Etiqueta y campo de entrada para el ID de la cámara
    label_camera_id = tk.Label(config_window, text="ID de la Cámara:")
    entry_camera_id = tk.Entry(config_window)

    # Botón para aplicar la configuración
    apply_button = tk.Button(
        config_window,
        text="Aplicar",
        command=lambda: apply_configuration(entry_camera_id.get()),
    )

    # Colocar etiqueta y campo de entrada en la ventana
    label_camera_id.grid(row=0, column=0)
    entry_camera_id.grid(row=0, column=1)
    apply_button.grid(row=1, columnspan=2)

# Función para aplicar la configuración de la cámara
def apply_configuration(camera_id):
    try:
        camera_id = int(camera_id)

        if camera_id not in cameras:
            cameras.append(camera_id)
            messagebox.showinfo("Configuración Exitosa", "Cámara configurada con éxito.")
        else:
            messagebox.showinfo("Advertencia", "Esta cámara ya ha sido agregada.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un ID de cámara válido.")

# Función para mostrar cámaras seleccionadas
def show_selected_cameras():
    for i, camera_id in enumerate(cameras):
        if i < len(canvas_list):
            canvas_list[i].config(state=tk.NORMAL)
            start_camera_thread(i, camera_id)

# Función para iniciar un hilo de cámara
def start_camera_thread(canvas_index, camera_id):
    camera_thread = threading.Thread(target=capture_camera, args=(camera_id, canvas_list[canvas_index]))
    camera_thread.daemon = True
    camera_thread.start()

# Función para cerrar la ventana de manera segura
def close_window():
    root.destroy()

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Cámaras en Tkinter")
etiqueta = tk.Label(text="Hola mundo")
etiqueta.pack()
# Botón para abrir la ventana de configuración de la cámara
config_button = tk.Button(root, text="Configurar Cámara", command=configure_camera)
config_button.pack()

# Botón para mostrar las cámaras seleccionadas
show_button = tk.Button(root, text="Mostrar Cámaras Seleccionadas", command=show_selected_cameras)
show_button.pack()

# Botón de salida
exit_button = tk.Button(root, text="Salir", command=close_window)
exit_button.pack()
# Lista para almacenar los ID de cámaras
cameras = []

# Configuración de los lienzos para mostrar las imágenes de las cámaras
canvas_list = []
for _ in range(6):
    canvas = tk.Canvas(root, width=800, height=600)
    canvas_list.append(canvas)
    canvas.pack()

# Ejecuta el bucle principal de Tkinter
root.mainloop()
