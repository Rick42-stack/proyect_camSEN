from tkinter import *
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

# Función para capturar imágenes de la cámara en un hilo separado
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

# Función para cerrar la ventana de manera segura
def close_window():
    ventana.destroy()

def expand_window():
    ventana.attributes("-fullscreen", True)

def restaurar_pantalla():
    ventana.attributes("-fullscreen", False)


# Configuración de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Cámaras en Tkinter")

menuBar = Menu(ventana)

ventana.config(menu=menuBar)

SistemaMenu = Menu(menuBar)

SistemaMenu.add_command(label="nueva cámara")
SistemaMenu.add_command(label="Resolución")
SistemaMenu.add_command(label="Guardar")
SistemaMenu.add_command(label="Restaurar valores predeterminados")
SistemaMenu.add_separator()
SistemaMenu.add_command(label="Salir")


editMenu = Menu(menuBar)

editMenu.add_command(label="Recortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

menuBar.add_cascade(label="Sistema", menu=SistemaMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)


# Configuración de los lienzos para mostrar las imágenes de las cámaras
canvas1 = tk.Canvas(ventana, width=640, height=480)
canvas1.pack()

#canvas2 = tk.Canvas(ventana, width=640, height=480)
#canvas2.pack()

#canvas3 = tk.Canvas(ventana, width=640, height=480)
#canvas3.pack()

#canvas4 = tk.Canvas(ventana, width=640, height=480)
#canvas4.pack()

# Configuración de los botones de salida para cada cámara
exit_button = tk.Button(ventana, text="Salir", command=close_window)
expand_button = tk.Button(ventana, text="Fullscreen", command=expand_window)
restore_button = tk.Button(ventana, text="Restore", command=restaurar_pantalla)
exit_button.place(x=480, y=320)
expand_button.pack()
restore_button.pack()

# Inicia la captura de las cámaras en hilos separados
camera_thread1 = threading.Thread(target=capture_camera, args=(0, canvas1))
#camera_thread2 = threading.Thread(target=capture_camera, args=("79.mp4", canvas2))
#camera_thread3 = threading.Thread(target=capture_camera, args=("79.mp4", canvas3))
#camera_thread4 = threading.Thread(target=capture_camera, args=("79.mp4", canvas4))

camera_thread1.daemon = True
#camera_thread2.daemon = True
#camera_thread3.daemon = True
#camera_thread4.daemon = True

camera_thread1.start()
#camera_thread2.start()
#camera_thread3.start()
#camera_thread4.start()

# Ejecuta el bucle principal de Tkinter
ventana.mainloop()






