import cv2
import vlc

# URL de la cámara IP (asegúrate de que sea una URL de transmisión de video)
url = "rtsp://admin:Dormamu290@192.168.0.20:554/onvif1?tcp"

# Crea un objeto VideoCapture con la URL
cap = cv2.VideoCapture(url)

# Verifica si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara IP.")
else:
    while True:
        # Captura un fotograma de la cámara IP
        ret, frame = cap.read()

        # Verifica si se capturó el fotograma correctamente
        if not ret:
            print("No se pudo capturar el fotograma.")
            break

        # Muestra el fotograma en una ventana
        cv2.imshow('Cámara IP', frame)

        # Sale del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Libera los recursos y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
