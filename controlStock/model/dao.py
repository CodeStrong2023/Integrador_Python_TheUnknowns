# from .conexionDB import Conexion
from tkinter import messagebox
import psycopg2 as bd #Esto es para poder conectar a Postgre
conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='productos')

## creacion de tabla

def crear_tabla():
    try:
        #conexion.autocommit = True 'NO ES UNA BUENA PRACTICA'
        cursor = conexion.cursor()
        sentencia ="""CREATE TABLE productos (
                id_productos SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                cantidad INTEGER,
                precio INTEGER)"""

        cursor.execute(sentencia)
        conexion.commit() #Hacemos el commit manualmente
        print('Base de datos creada con exito...')
        titulo = "Crear producto"
        mensaje= "La base de datos se creo con Exito"
        messagebox.showinfo(titulo, mensaje)
        print(cursor.execute("SELECT * FROM productos"))
        
    except Exception as e:
        conexion.rollback()
        print(f'Ocurrio un error, se hizo un rollback: {e}')
    


def borrar_tabla():
        try:
            #conexion.autocommit = True 'NO ES UNA BUENA PRACTICA'
            cursor = conexion.cursor()
            sentencia ="DROP TABLE productos"

            cursor.execute(sentencia)
            conexion.commit() #Hacemos el commit manualmente
            print('Base de datos ELIMINADA')
            titulo = "Crear producto"
            mensaje= "La tabla se borro correctamente"
            messagebox.showwarning(titulo, mensaje)
            
        except Exception as e:
            conexion.rollback()
            print(f'Ocurrio un error, se hizo un rollback: {e}')


def guardar(nombre,cantidad,precio):
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'INSERT INTO productos (nombre, cantidad, precio) VALUES (%s,%s,%s)'
                    valores= (nombre,  cantidad, precio) #es una tupla
                    cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
                    conexion.commit() #esto se utiliza para guardar los cambios en la base de datos
                    titulo = "Crear producto"
                    mensaje= "Producto agregado con exito"
                    messagebox.showinfo(titulo, mensaje)
                    registros_insertados = cursor.rowcount
                    print(f'Los registros insertados son: {registros_insertados}')
                    print(f"{nombre}, {cantidad},{precio}")

        except Exception as e:
                titulo = "Crear producto"
                mensaje= "Error"
                messagebox.showerror(titulo, mensaje)
                print(f'Ocurrio un error: {e}')
                
#LISTAR PRODUCTOS

def mostrar_producto():
    
        sentencia = "SELECT * FROM productos ORDER BY id_productos DESC"
        lista=[]
    
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(sentencia)
                    lista = cursor.fetchall()
                    return lista
                
        except Exception as e:
                    print(f'Ocurrio un error: {e}')
                    titulo = "Mostrar productos"
                    mensaje= "Error! La tabla no existe"
                    messagebox.showerror(titulo, mensaje)

#EDITAR PRODUCTOS

def editar(nombre, cantidad, precio, id_producto):
    
        print(nombre, cantidad, precio, id_producto)
        with conexion:
                with conexion.cursor() as cursor:
                    sentencia = """UPDATE productos SET 
                                nombre = %s,
                                cantidad = %s, 
                                precio = %s 
                                WHERE id_productos = %s"""
                    valores= ( nombre,  cantidad, precio, id_producto)
                    cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
                    conexion.commit() #esto se utiliza para guardar los cambios en la base de datos
                    titulo = "Crear producto"
                    mensaje= "Producto editado con exito"
                    messagebox.showinfo(titulo, mensaje)

def eliminar(id_producto):
    print(id_producto)
    with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'DELETE FROM productos WHERE id_productos = %s'
                    cursor.execute(sentencia, (id_producto,))
                    conexion.commit() #esto se utiliza para guardar los cambios en la base de datos
                    titulo = "Eliminar Producto"
                    mensaje= "Producto Eliminado con exito"
                    messagebox.showwarning(titulo, mensaje)


