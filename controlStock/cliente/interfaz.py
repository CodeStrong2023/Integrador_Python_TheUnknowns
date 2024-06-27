import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from model.dao import crear_tabla, borrar_tabla, editar, eliminar, guardar, mostrar_producto
    
############# VENTANA PRINCIPAL ########################

#Creacion de Frame: espacio que va a contener las etiquetas o labels dentro de la ventana

#heredamos la clase frame
class frame_main(tk.Frame):
    
    
    def __init__(self, root):
        super().__init__(root) 
        self.root = root
        self.pack()
        self.mensaje()
        self.tabla_productos()
        self.botones()
        self.campos()
        self.id_productos = None
                
    def mensaje(self):
        self.label_nombre = tk.Label(self, text= 'Lista de Productos') #se le da nombre 'producto' a la etiqueta
        self.label_nombre.config(font=('Arial',12, 'bold')) #modificamos letra, tamaño, tipo
        self.label_nombre.grid(row=0, column=0, padx=0, pady=0) #metodo grid para ubicar la etiqueta dentro del frame con filas/columnas
    
    #Creacion de la tabla
    def tabla_productos(self):
        #traemos la lista de productos a la tabla
        self.lista = mostrar_producto()
        
        #se crea la tabla
        self.tabla=ttk.Treeview(self, column=("Producto", "Cantidad", "Precio")) #campos
        #posicion de la tabla en la ventana
        self.tabla.grid(row=1,column=0, columnspan=2)

        #encabezado de la rabla
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Producto')
        self.tabla.heading('#2',text='Cantidad')
        self.tabla.heading('#3',text='Precio')
        try:
            #iteramos los productos
            for i in self.lista:
                #agregando datos a la tabla
                self.tabla.insert('', 0, text=i[0], 
                values=( i[1] , i[2], i[3]))
        except:
            titulo = "Mostrar productos"
            mensaje= "Error! La tabla no existe, cree la tabla nueva"
            messagebox.showerror(titulo, mensaje)
        
    # BOTONES
    def botones(self):    
        self.boton_actualizar= tk.Button(self,text='Actualizar', command=self.tabla_productos) 
        self.boton_actualizar.config(width=20, font=('Arial',12,'bold'), 
            fg='white', bg='blue',
            cursor='hand2',  
            activebackground='#B96161',
            activeforeground='white')
        self.boton_actualizar.grid(row=2, column=0,pady=5)
        
        self.boton_editar= tk.Button(self,text='Editar', command = self.editar_producto) 
        self.boton_editar.config(width=20, font=('Arial',12,'bold'), 
                            fg='white', bg='green',
                            cursor='hand2',  
                            activebackground='#35BD6F',
                            activeforeground='white',) 
        self.boton_editar.grid(row=2, column=1,pady=5, columnspan=1)
        
        self.boton_eliminar= tk.Button(self,text='Eliminar', command= self.eliminar_producto) 
        self.boton_eliminar.config(width=20, font=('Arial',12,'bold'), 
                            fg='white', bg='red',
                            cursor='hand2',  
                            activebackground='#B96161', 
                            activeforeground='white') 
        self.boton_eliminar.grid(row=7, column=1, padx=0, pady=5)
        
        
        self.boton_guardar= tk.Button(self,text='Guardar', command= self.guardar_producto) 
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'), 
                            fg='white', bg='green',
                            cursor='hand2',  
                            activebackground='#35BD6F',
                            activeforeground='white',) 
        self.boton_guardar.grid(row=7, column=0, padx=5, pady=5)
    
    
    def campos(self):
        self.label_nombre = tk.Label(self, text= 'Producto') #se le da nombre 'producto' a la etiqueta
        self.label_nombre.config(font=('Arial',12, 'bold')) #modificamos letra, tamaño, tipo
        self.label_nombre.grid(row=4, column=0, padx=10, pady=10) #metodo grid para ubicar la etiqueta dentro del frame con filas/columnas
        
        self.label_cantidad = tk.Label(self, text= 'Cantidad') 
        self.label_cantidad.config(font=('Arial',12, 'bold')) 
        self.label_cantidad.grid(row=5, column=0, padx=10, pady=10) # pad x/y son los padding en cada eje
        
        self.label_precio = tk.Label(self, text= 'Precio') 
        self.label_precio.config(font=('Arial',12, 'bold')) 
        self.label_precio.grid(row=6, column=0, padx=10, pady=10)#columnspan cantidad de columnas que ocupa el campo
        
        #Se crean los campos inputs
        self.nombre_prod=tk.StringVar() #Stringvar se utiliza para enviar valores al campo. para limpiar se mandan valores vacios
        self.input_nombre = tk.Entry(self, textvariable= self.nombre_prod) #textvariable= self.nombre) se crea el objeto input con tk.Entry // textvariable: llama al objeto Stringvar
        self.input_nombre.config(width=20, font=('Arial',12), state='disabled')
        self.input_nombre.grid(row=4, column=1,padx=8, pady=10, columnspan=2)
        
        self.cantidad_prod=tk.IntVar()
        self.input_cantidad = tk.Entry(self, textvariable= self.cantidad_prod)  
        self.input_cantidad.config(width=20, font=('Arial',12), state='disabled') #State es para habilitar o deshabilitar la escritura
        self.input_cantidad.grid(row=5, column=1,padx=5, pady=10, columnspan=2)
        
        self.precio_prod=tk.IntVar()
        self.input_precio = tk.Entry(self, textvariable= self.precio_prod)  
        self.input_precio.config(width=20, font=('Arial',12), state='disabled')
        self.input_precio.grid(row=6, column=1,padx=5, pady=10, columnspan=2)
    
    def editar_producto(self):
        try:
            self.id_productos = self.tabla.item(self.tabla.selection())['text']
            self.producto = self.tabla.item(self.tabla.selection())['values'][0]
            self.cantidad = self.tabla.item(self.tabla.selection())['values'][1]
            self.precio = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.input_nombre.config(state='normal')
            self.input_cantidad.config(state='normal')
            self.input_precio.config(state='normal')
                
            self.input_nombre.insert(0,self.producto)
            self.input_cantidad.insert(0,self.cantidad)
            self.input_precio.insert(0,self.precio)
        except:
            titulo = "Editar producto"
            mensaje= "No se ha seleccionado ningun producto"
            messagebox.showwarning(titulo, mensaje)
        
    def guardar_producto(self):
        try:
            editar(self.nombre_prod.get(),self.cantidad_prod.get(),self.precio_prod.get(), self.id_productos)
            
            self.nombre_prod.set(' ')
            self.precio_prod.set(' ')
            self.cantidad_prod.set(' ')
            
            self.input_nombre.config(state='disabled')
            self.input_cantidad.config(state='disabled')
            self.input_precio.config(state='disabled')
            
        except:
            titulo = "Guardar producto"
            mensaje= "No hay datos para guardar"
            messagebox.showwarning(titulo, mensaje)
        
        
    def eliminar_producto(self):
        try:
            self.id_productos = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_productos)
        except:
            titulo = "Eliminar producto"
            mensaje= "No se ha seleccionado ningun producto"
            messagebox.showwarning(titulo, mensaje)