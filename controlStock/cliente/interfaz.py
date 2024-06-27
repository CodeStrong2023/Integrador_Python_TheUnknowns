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
            
            
######################## Barra de menu
def menu(root):
    #instancia de la clase menu
    menu = tk.Menu(root) 
    #se fija a la ventana root
    root.config(menu=menu, width=600, height=500)
    
    ##PARA AGREGAR MAS MENU A LA VENTANA SE REPITEN LOS PROCESOS A CONTINUACION:  
    
    #se crea la primer pestaña de la barra de menu
    menu_principal = tk.Menu(menu, tearoff= 0) #tearoff borra la linea punteada al principio del menu
    menu.add_cascade(label= 'Archivo', menu = menu_principal) #menu desplegable
    #etiquetas del menu desplegable
    menu_principal.add_command(label ='Nuevo producto', command=nuevo_producto)
    menu_principal.add_command(label ='Eliminar producto')
    menu_principal.add_separator()
    menu_principal.add_command(label ='Salir', command=root.destroy) #comman= root.destroy para cerrar el programa
    
    #MENU BASE DE DATOS
    menu_database = tk.Menu(menu, tearoff= 0)
    menu.add_cascade(label= 'Base de datos', menu=menu_database)
    menu_database.add_command(label='Crear base de datos', command= crear_tabla)
    menu_database.add_command(label='Borrar base de datos', command= borrar_tabla)    
    
    
    #menu ayuda
    ayuda=tk.Menu(menu, tearoff=0) 
    menu.add_cascade(label='Ayuda', menu=ayuda)
    ayuda.add_command(label='Sobre nosotros...', command= about) #se llama a la funcion para mostrar el mensaje
    
#sobre nosotros
def about():
    messagebox.showinfo('about',"""
Grupo: TheUnknowns
LEGAJOS
Riera Arturo 10493
Belich Juan Ignacio 10338
Bilyk María sol 10341
Ravanal Lautaro emanuel 10490
""") # titulo, mensaje a mostrar en la nueva ventana
    
    


#######################  VENTANA SECUNDARIA ##############################
## Creacion de ventana secundaria con Toplevel()
def nuevo_producto():
    ventana = Toplevel()
    ventana.geometry('500x200')
    ventana.resizable(0,0)
    #uso de la clase frame, se le pasa como parametro la ventana secundaria
    frame(root=ventana)
    
class frame(tk.Frame):    
    
    def __init__(self, root):
        
        #heredamos el constructor de la clase padre frame
        super().__init__(root,width= 700, height=500) #se le pueden enviar configuraciones de frame como .config()
        self.root = root
        self.pack() # se empaqueta el frame dentro de la ventana
        # self.config(width= 700, height=500, bg='grey') #configuracion del tamaño del frame, la ventana va a tomar el tamaño del frame
        self.nombre_campos(root) #llamamos a la funcion campos para integrar la etiqueta al frame
        
        
        
    def nombre_campos(self, root):
        #se crean las etiquetas de los campos
        self.label_nombre = tk.Label(self, text= 'Producto') #se le da nombre 'producto' a la etiqueta
        self.label_nombre.config(font=('Arial',12, 'bold')) #modificamos letra, tamaño, tipo
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10) #metodo grid para ubicar la etiqueta dentro del frame con filas/columnas
        
        self.label_cantidad = tk.Label(self, text= 'Cantidad') 
        self.label_cantidad.config(font=('Arial',12, 'bold')) 
        self.label_cantidad.grid(row=1, column=0, padx=10, pady=10) # pad x/y son los padding en cada eje
        
        self.label_precio = tk.Label(self, text= 'Precio') 
        self.label_precio.config(font=('Arial',12, 'bold')) 
        self.label_precio.grid(row=2, column=0, padx=10, pady=10)#columnspan cantidad de columnas que ocupa el campo
        
        #Se crean los campos inputs
        self.nombre=tk.StringVar() #Stringvar se utiliza para enviar valores al campo. para limpiar se mandan valores vacios
        self.input_nombre = tk.Entry(self, textvariable = self.nombre) #textvariable= self.nombre) se crea el objeto input con tk.Entry // textvariable: llama al objeto Stringvar
        self.input_nombre.config(width=20, font=('Arial',12))
        self.input_nombre.grid(row=0, column=1,padx=8, pady=10, columnspan=2)
        
        self.cantidad=tk.IntVar()
        self.input_cantidad = tk.Entry(self, textvariable= self.cantidad)  
        self.input_cantidad.config(width=20, font=('Arial',12)) #State es para habilitar o deshabilitar la escritura
        self.input_cantidad.grid(row=1, column=1,padx=5, pady=10, columnspan=2)
        
        self.precio=tk.IntVar()
        self.input_precio = tk.Entry(self, textvariable= self.precio)  
        self.input_precio.config(width=20, font=('Arial',12))
        self.input_precio.grid(row=2, column=1,padx=5, pady=10, columnspan=2)
        
        #Botones
        self.boton_cancelar= tk.Button(self,text='Cancelar') # se crea el objeto boton
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'), 
                        fg='white', bg='red',# fg= color de letra
                        cursor='hand2', # cursor: cambia el cursos a mano cuando se pasa por arriba del boton 
                        activebackground='#B96161', #fondo cuando el boton se presiona
                        activeforeground='white',#color de letra cuando el boton se presiona
                        command=root.destroy) 
        self.boton_cancelar.grid(row=4, column=1, padx=10, pady=10) #posicion en el frame
        
        
        self.boton_aceptar= tk.Button(self, text='Aceptar', command=lambda: (self.guardar_producto(), root.destroy())) #funcion LAMNDA para ejecutar dos funciones
        self.boton_aceptar.config(width=20, font=('Arial',12,'bold'), 
                        fg='white', bg='green',
                        cursor='hand2',  
                        activebackground='#35BD6F',
                        activeforeground='white') 
        self.boton_aceptar.grid(row=4, column=0, padx=10, pady=10) 
        

    def guardar_producto(self):
        
        guardar(self.nombre.get(),self.cantidad.get(),self.precio.get())