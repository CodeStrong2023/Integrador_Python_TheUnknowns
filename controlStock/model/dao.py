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





