from tkinter import *
from tkinter import ttk
import pickle #PICKLE RICK!!!

root = Tk() #ventana principal/ventana raiz de la app
root.state('zoomed') #esta en pantalla completa
root.title("INCUCAI")
root.iconbitmap(r"C:\Users\Usuario\Downloads\Viera-Wessolowski\src\logo-incucai.ico") 
root.configure(bg="navajowhite") #color de fondo

root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root.config(menu=menubar)

menu_Centro_salud = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=menu_Centro_salud, label='Centro de Salud')
menu_Centro_salud.add_command(label='Agregar centro')
menu_Centro_salud.add_command(label='Listar centros')

menu_Donante = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=menu_Donante, label='Donante')
menu_Donante.add_command(label='Agregar donante')
menu_Donante.add_command(label='Listar donantes')

menu_Receptor = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=menu_Receptor, label='Receptor')
menu_Receptor.add_command(label='Agregar receptor')
menu_Receptor.add_command(label='Listar receptores')


root.mainloop()

#def agregar_centro_salud():
#   pass