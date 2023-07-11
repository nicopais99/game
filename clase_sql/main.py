import sqlite3
id = 5
sueldo = 500
with sqlite3.connect("mi_base_de_datos.db") as conexion:
    try:
        # sentencia = "update Empleados set sueldo = ? where id = ?"
        sentencia = "delete from Empleados where sueldo < 1000"
        #create table
        # sentencia = """
        #             create table Empleados
        #             (
        #                 id integer primary key autoincrement,
        #                 nombre text,
        #                 apellido text,
        #                 sueldo real 
        #             )
        #             """
        nombre = "Martin"
        apellido = "Gomez"
        sueldo = 30247
        direccion = "Avenida siempreviva 123"
        # sentencia = """
        # insert into Empleados(nombre, apellido, sueldo, direccion) values(?,?,?,?)            
        # """
        # sentencia = "select * from Empleados order by sueldo desc limit 3"
        cursor = conexion.execute(sentencia)
        print("Tabla creada con exito")
    except:
        print("Error!!")

        """
        INSERT into tabla([lista_campos]) values(lista_valores)

        SELECT nombre, apellido
        From Empleados
        WHERE sueldo > 50000
        [Order by asc|desc]

        'UPDATE Tabla set campo = valor [WHERE condicion]'

        DELETE from Tabla where condicion
        """

