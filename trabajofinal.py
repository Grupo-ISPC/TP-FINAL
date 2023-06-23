import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = 'root', 
                                   host = 'localhost',
                                   database = 'normativa',
                                   port = '3306')

#OPCION 1 MUESTRA todo lo que tenemos en la base de datos
class Normativas:
    def __init__ (self, registro = None, numeronormativa = None, fecha = None, descripcion = None, idtiponormativa = None, idcategoria = None, idjurisdiccion = None):

        self.registro = registro
        self.numeronormativa = numeronormativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.idtiponormativa = idtiponormativa
        self.idcategoria = idcategoria
        self.idjurisdiccion = idjurisdiccion


    @staticmethod
    def mostrar_registros():
       
        # Cursor
        cursor = conexion.cursor()

        # Ejecutar consulta SQL
        cursor.execute("SELECT * FROM normativas")

        # Obtener todos los registros
        registros = cursor.fetchall()

        # Mostrar los registros
        for registro in registros:
            print("Número de Registro:", registro[0])
            print("Número de Normativa:", registro[1])
            print("Fecha:", registro[2])
            print("Descripción:", registro[3])
            print("ID de Normativa:", registro[4])
            print("ID de Categoría:", registro[5])
            print("ID de Jurisdicción:", registro[6])
            print("--------------------")

        # Cerrar cursor y conexión a la base de datos
        #cursor.close()
       # conexion.close()

#OPCION 2 AGREGAR un nuevo registro a la base de datos
class Insertar:
    cursor = conexion.cursor()

    def __init__(self):
        self.numero_normativa = None
        self.fecha = None
        self.descripcion1 = None
        self.id_tiponormativa = None
        self.id_categoria = None
        self.id_jurisdiccion = None

    def mostrar(self):
        cursor = conexion.cursor()

        self.numero_normativa = input("Ingrese el número de normativa: ")
        self.fecha = input("Ingrese la fecha de sanción de la normativa con este formato YYYY-MM-DD: ")
        self.descripcion1 = input("Ingrese una descripción de hasta 400 caracteres: ")
        self.id_tiponormativa = input("Normativa= ingrese 500 para LEY, 501 para DECRETO y 502 para RESOLUCIÓN: ")
        self.id_categoria = input("Categoria= ingrese 200 para LABORAL, 201 PENAL, 202 CIVIL, 203 COMECIAL, 204 FAMILIAS Y SUCESIONES, 205 AGRARIO Y AMBIENTAL, 206 MINERIA, 207 DERECHO INFORMATICO: ")
        self.id_jurisdiccion = input("Jurisdiccion= ingrese 300 para NACIONAL y 301 para PROVINCIAL: ")

        

        
        # Ejecutar consulta SQL
        sentencia = "INSERT INTO normativas (Numero, Fecha, Descripcion, Tipo_normativa_idTipo_normativa, Categoria_idCategoria, Jurisdiccion_idJurisdiccion) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')" .format(self.numero_normativa, self.fecha, self.descripcion1, self.id_tiponormativa, self.id_categoria, self.id_jurisdiccion)
        cursor.execute(sentencia)
        conexion.commit()

#OPCION 3 ACTUALIZAR un registro completo
def actualizar():
    cursor = conexion.cursor()


    numero_registro = input("Ingrese el numero de registro que desea cambiar: ")
    numero_normativa = input("Ingrese el número de normativa: ")
    fecha = input("Ingrese la fecha de sanción de la normativa con este formato YYYY-MM-DD: ")
    descripcion1 = input("Ingrese una descripción de hasta 400 caracteres: ")
    id_tiponormativa = input("Normativa= ingrese 500 para LEY, 501 para DECRETO y 502 para RESOLUCIÓN: ")
    id_categoria = input("Categoria= ingrese 200 para LABORAL, 201 PENAL, 202 CIVIL, 203 COMECIAL, 204 FAMILIAS Y SUCESIONES, 205 AGRARIO Y AMBIENTAL, 206 MINERIA, 207 DERECHO INFORMATICO: ")
    id_jurisdiccion = input("Jurisdiccion= ingrese 300 para NACIONAL y 301 para PROVINCIAL: ")


    # Ejecutar consulta SQL
    sentencia = """UPDATE normativas SET Numero = '{}', Fecha = '{}', Descripcion = '{}', Tipo_normativa_idTipo_normativa = '{}', Categoria_idCategoria = '{}', Jurisdiccion_idJurisdiccion = '{}' WHERE Numero_Registro = '{}' """. format(numero_normativa, fecha, descripcion1, id_tiponormativa, id_categoria, id_jurisdiccion, numero_registro)
    cursor.execute(sentencia)
    conexion.commit()

    #cursor.close()
    #conexion.close()

#OPCION 4 ELIMINAR un registro completo
def eliminar():
    
    cursor = conexion.cursor()
    
    registro_eliminar = input("Ingrese el número de normativa que desea eliminar: ")

    # Ejecutar consulta SQL
    sentencia = "DELETE FROM normativas WHERE Numero = ('{}')".format(registro_eliminar)
    cursor.execute(sentencia)
    conexion.commit()

    #cursor.close()
    #conexion.close()

#OPCION 5 buscar 
def buscar():
    cursor = conexion.cursor()

    ingresoUsuario = input('Ingrese como desea buscar 1 - Numero de ley o  2 - Palabra clave: ')

    if ingresoUsuario == '1':
        buscar = input("Ingrese el numero de normativa que desea buscar: ")
         #Ejecutar consulta SQL 
        sentencia = "SELECT * FROM normativas WHERE Numero = '{}'".format(buscar)
    elif ingresoUsuario == '2':
        palabraClave = input('Ingrese palabra clave: ')
        #Ejecutar SQL
        sentenciaAuxiliar = "SELECT idPalabra_clave FROM palabra_clave WHERE palabra = '{}'".format(palabraClave)

        cursor.execute(sentenciaAuxiliar)
        temporal = cursor.fetchone()
        

        sentenciaAuxiliar2 = "SELECT Normativa_Numero_registro FROM normativa_has_palabra_clave WHERE Palabra_clave_idPalabra_clave = '{}'".format(temporal[0])

        cursor.execute(sentenciaAuxiliar2)
        temporal2 = cursor.fetchone()
        

        sentencia = "SELECT * FROM normativas WHERE Numero_registro = '{}'".format(temporal2[0])       
    else:
        print('Ingrese una opcion valida')
        return buscar()


     
    cursor.execute(sentencia)

    # Obtener todos los registros
    registros = cursor.fetchall()
      
    # Mostrar los registros
    for registro in registros:
            print("Número de Registro:", registro[0])
            print("Número de Normativa:", registro[1])
            print("Fecha:", registro[2])
            print("Descripción:", registro[3])
            print("ID de Normativa:", registro[4])
            print("ID de Categoría:", registro[5])
            print("ID de Jurisdicción:", registro[6])
            print("--------------------")


     
    #cursor.close()
    #conexion.close()

#MENU QUE SE MUESTRA EN CONSOLA 
def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Mostrar Registro: ")
    print("2. Agregar Registro: ")
    print("3. Actualizar Registro: ")
    print("4. Eliminar Registro: ")
    print("5. Buscar por numero de normativa o palabra clave: ")
    print("6. Salir")
    print("--------------")

#MENU CON TODAS SUS OPCIONES 
while True:

    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        #MOSTRAR TODOS LOS REGISTROS 
        leyes = Normativas(registro = None, numeronormativa = None, fecha = None, descripcion = None, idtiponormativa = None, idcategoria = None, idjurisdiccion = None)
        leyes.mostrar_registros()
        print('------------------------')
    

    elif opcion == "2":
        #INGRESAR UN NUEVO REGISTRO
        nuevo = Insertar()
        nuevo.mostrar()
        print("Su registro fue exitoso")
        print('------------------------')


    elif opcion == "3":
        #ACTUALIZAR REGISTRO
        actualizar()
        print("La actualizacion fue exitosa")
        print('------------------------')


    elif opcion == "4":
        #BORRAR REGISTRO POR NUMERO DE NORMATIVA
        eliminar()
        print("Se elimino correctamente")
        print('------------------------')
       

    elif opcion == "5":
        #BUSCAR POR NUMERO DE NORMATIVA O PALABRA CLAVE
        buscar()
        print("El registro se busco correctamente ")
        print('------------------------')
        
        
    elif opcion == "6":
        #SALIR
        conexion.close()
        print("Gracias por usar nuestra base de datos")
        print('------------------------')

        break

    else:
        print("Seleccione una opcion valida")
        print('------------------------')
        



        



        

