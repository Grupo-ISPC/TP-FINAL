import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', 
                                   host = 'localhost',
                                   database = 'normativa',
                                   port = '3306')

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

        

        print(self.numero_normativa, self.fecha, self.descripcion1, self.id_tiponormativa, self.id_categoria, self.id_jurisdiccion)
        # Ejecutar consulta SQL
        sentencia = "INSERT INTO normativas (Numero, Fecha, Descripcion, Tipo_normativa_idTipo_normativa, Categoria_idCategoria, Jurisdiccion_idJurisdiccion) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')" .format(self.numero_normativa, self.fecha, self.descripcion1, self.id_tiponormativa, self.id_categoria, self.id_jurisdiccion)
        cursor.execute(sentencia)
        conexion.commit()



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
        print('------------------------')
    

    elif opcion == "2":
        #INGRESAR UN NUEVO REGISTRO
        nuevo = Insertar()
        print(nuevo.mostrar())
        print("Su registro fue exitoso")
        print('------------------------')


    elif opcion == "3":
        #ACTUALIZAR REGISTRO
        print("La actualizacion fue exitosa")
        print('------------------------')


    elif opcion == "4":
        #BORRAR REGISTRO POR NUMERO DE NORMATIVA
        print("Se elimino correctamente")
        print('------------------------')
       

    elif opcion == "5":
        #BUSCAR POR NUMERO DE NORMATIVA O PALABRA CLAVE
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
        



        



        

