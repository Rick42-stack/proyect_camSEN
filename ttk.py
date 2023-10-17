import cv2
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout

class CameraViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EQUIPATE Camera Interface")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.camera_frames = []
        self.capture_objects = []
        self.add_buttons = []
        self.remove_buttons = []  # Lista para los botones de eliminación

        rows = 2
        cols = 3

        for row in range(rows):
            for col in range(cols):
                camera_widget = QWidget()
                camera_layout = QVBoxLayout()
                camera_widget.setLayout(camera_layout)

                frame_label = QLabel(self)
                camera_layout.addWidget(frame_label)
                self.camera_frames.append(frame_label)

                add_button = QPushButton("Agregar Cámara", self)
                add_button.clicked.connect(self.add_camera)
                camera_layout.addWidget(add_button)
                self.add_buttons.append(add_button)

                remove_button = QPushButton("Eliminar Cámara", self)
                remove_button.clicked.connect(lambda _, index=len(self.remove_buttons): self.remove_camera(index))
                camera_layout.addWidget(remove_button)
                self.remove_buttons.append(remove_button)

                self.layout.addWidget(camera_widget, row, col)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update)
        self.update_timer.start(100)

    def add_camera(self):
        for i, button in enumerate(self.add_buttons):
            if button is self.sender():
                if len(self.capture_objects) < len(self.camera_frames):
                    cap = cv2.VideoCapture(len(self.capture_objects))
                    if cap.isOpened():
                        self.capture_objects.append(cap)
                        button.setDisabled(True)
                        self.remove_buttons[i].setEnabled(True)  # Habilitar el botón de eliminación
                break

    def remove_camera(self, index):
        if 0 <= index < len(self.capture_objects):
            self.capture_objects[index].release()
            self.capture_objects.pop(index)
            self.add_buttons[index].setEnabled(True)
            self.remove_buttons[index].setEnabled(False)  # Deshabilitar el botón de eliminación

    def update(self):
        for i, cap in enumerate(self.capture_objects):
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)
                self.camera_frames[i].setPixmap(pixmap)
                self.camera_frames[i].setAlignment(Qt.AlignCenter)
            else:
                self.camera_frames[i].setText("Cámara {} no disponible".format(i))
                self.capture_objects[i] = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CameraViewer()
    viewer.show()
    sys.exit(app.exec_())
