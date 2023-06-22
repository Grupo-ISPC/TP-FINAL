import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', 
                                   host = 'localhost',
                                   database = 'normativa',
                                   port = '3306')

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
        actualizar()
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
        



        

