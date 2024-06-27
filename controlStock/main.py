from tkinter import *
import tkinter as tk
from cliente.interfaz import *

def main():
    #ventana raiz
    root = tk.Tk()
    root.title('Control de Stock') #Titulo de la ventana
    root.iconbitmap('img/icono.ico') #Icono en el titulo de la ventana
    root.resizable(0,0) # permite si los valores son 1 poder redimensionar la ventana, si son 0 no se puede modificar
    root.geometry("800x500") #redimensionar ventana raiz
    
    
    menu(root) #llamamos a la clase menu para agregar los menu desplegables a la ventana raiz
    interfaz = frame_main(root=root)# uso de la clase frame, se le pasa como parametro la ventana principal
    
    
    
    interfaz.mainloop() #funcion ejecutar la ventana

if __name__ == '__main__':
    main()