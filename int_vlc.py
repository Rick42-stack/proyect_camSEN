from tkinter import *
import tkinter as tk
import vlc
from PIL import Image, ImageTk
import time
import cv2


# URL RTSP de tu cámara IP
rtsp_url = "rtsp://admin:Dormamu290@192.168.0.41:554/onvif1"

# Crear una instancia de VLC
instance = vlc.Instance("--no-xlib")

# Crear un reproductor VLC
player = instance.media_player_new()
media = instance.media_new(rtsp_url)
media.get_mrl()
player.set_media(media)

# Crear una ventana Tkinter
root = tk.Tk()
root.title("Reproducción de Cámara IP")

# Obtener el control de la ventana de reproductor de VLC
win_id = player.get_hwnd()
if win_id:
    player.set_hwnd(win_id)

# Configurar la ventana Tkinter
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Iniciar la reproducción
player.play()

# Función para cerrar la ventana
def on_closing(rtsp_url, canvas):
    player.stop()
    root.destroy()

    # Para que la cámara IP se vea dentro de la ventana Tkinter
    # Capturar imágenes de la cámara IP
    cap = cv2.VideoCapture(rtsp_url)

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

    

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
