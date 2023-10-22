from tkinter import *
import tkinter as tk
import vlc

rtsp_url = "rtsp://admin:Dormamu290@192.168.0.41:554/onvif1"

ventana = tk.Tk()
ventana.title("VLC in Tkinter")

# Recording flag
is_recording = False

def toggle_recording():
    global is_recording
    if is_recording:
        # Stop recording
        media.add_option(":sout-keep")
        is_recording = False
        
    else:
        # Start recording
        media.add_option(":sout=#transcode{vcodec=h264,acodec=mp3,ab=128,samplerate=44100}:duplicate{dst=std{access=file,mux=mp4,dst='video.mp4'}}")
        is_recording = True


def stop_recording():
    global is_recording
    media.add_option(":sout-keep")
    is_recording = False
    # The recorded video will be saved to video.mp4 when recording is stopped


# Principal Menu
menuBar = Menu(ventana)

ventana.config(menu=menuBar)

archivoMenu = Menu(menuBar)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()

# Add recording button
record_button = archivoMenu.add_command(label="Grabar", command=toggle_recording)
# Add stop recording button
stop_recording_button = archivoMenu.add_command(label="Detener grabación", command=stop_recording)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")


editMenu = Menu(menuBar)

editMenu.add_command(label="Recortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)


instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(rtsp_url)
media.get_mrl()
player.set_media(media)


# Create Canvas for Video Playback:
canvas = tk.Canvas(ventana, width=640, height=480)
canvas.grid(row=2, column=1)

# Create Frame for Embedding VLC:
video_frame = tk.Frame(canvas)
video_frame.pack()

# Get and Set VLC Window ID:
win_id = canvas.winfo_id()
if win_id:
    player.set_hwnd(win_id)


# Position VLC Frame within Canvas:
canvas.create_window(0, 0, anchor="nw", window=video_frame)
player.play()
ventana.mainloop()


