import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', 
                                   host = 'localhost',
                                   database = 'normativa',
                                   port = '3306')

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
        



        



        

