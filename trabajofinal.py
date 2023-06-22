import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', 
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
        



        



        

   