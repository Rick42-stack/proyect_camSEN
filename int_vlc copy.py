import tkinter as tk
import vlc
import time

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
def on_closing():
    player.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
