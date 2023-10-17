from tkinter import *


ventana = Tk()


menuBar = Menu(ventana)

ventana.config(menu=menuBar)

archivoMenu = Menu(menuBar)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")


editMenu = Menu(menuBar)

editMenu.add_command(label="Recortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)

ventana.mainloop()
