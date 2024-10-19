clientes = {}

def main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Usuarios")
        print("2. Paquetes")
        print("3. Reserva de Vuelos")
        print("4. Reserva de Hoteles")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_principal_usuarios()
        elif opcion == '2':
            menu_paquetes()
        elif opcion == '3':
            reserva_v()
        elif opcion == '4':
            reserva_hoteles()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_principal_usuarios():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar Cliente")
        print("2. Iniciar Sesión")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            
#---------------------------------------------------  registrar clientes---------------------------------------------------            

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su número de teléfono: ")

    if not nombre or not apellido or not correo or not telefono:
        print("\nError: Todos los campos son obligatorios. Intente nuevamente.")
        return

    clientes[correo] = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono
    }
    print("\nCliente registrado con éxito!")

def iniciar_sesion():
    correo = input("Ingrese su correo para iniciar sesión: ")
    telefono = input("Ingrese su número de teléfono como contraseña: ")

    if correo in clientes and clientes[correo]['telefono'] == telefono:
        print(f"\nInicio de sesión exitoso. Bienvenido/a {clientes[correo]['nombre']} {clientes[correo]['apellido']}!")
    else:
        print("\nError: Correo o número de teléfono incorrectos.")

def modificar_cliente():
    correo = input("Ingrese el correo del cliente que desea modificar: ")

    if correo not in clientes:
        print("\nError: Cliente no encontrado.")
        return

    print("\n¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Correo")
    print("4. Teléfono")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        if nuevo_nombre:
            clientes[correo]['nombre'] = nuevo_nombre
            print("\nNombre actualizado con éxito!")
    elif opcion == '2':
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        if nuevo_apellido:
            clientes[correo]['apellido'] = nuevo_apellido
            print("\nApellido actualizado con éxito!")
    elif opcion == '3':
        nuevo_correo = input("Ingrese el nuevo correo: ")
        if nuevo_correo and nuevo_correo not in clientes:
            clientes[nuevo_correo] = clientes.pop(correo)
            print("\nCorreo actualizado con éxito!")
        else:
            print("\nError: El correo ingresado ya existe o no es válido.")
    elif opcion == '4':
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        if nuevo_telefono:
            clientes[correo]['telefono'] = nuevo_telefono
            print("\nTeléfono actualizado con éxito!")
    else:
        print("\nOpción no válida. Intente nuevamente.")

def eliminar_cliente():
    correo = input("Ingrese el correo del cliente que desea eliminar: ")

    if correo in clientes:
        del clientes[correo]
        print("\nCliente eliminado con éxito!")
    else:
        print("\nError: Cliente no encontrado.")

#---------------------------------------------------PAQUETES---------------------------------------------------

def menu_paquetes():
    paquete_t = []
    paquete_creado = []
    adicional_paquete = []

    while True:
        print("---------------MENU DE PAQUETES TURISTICOS--------------- \nSeleccione 1 opcion para ingresar al modulo\n------------------------------")
        print("1. Mostar paquetes")
        print("2. Crear paquete a su preferencia")
        print("3. Volver al Menú Principal")
        print("------------------------------")
        
        opcion = input("Eliga una opcion: ")

        if opcion == '1':
            while True:
                print("----------Paquetes mas vendidos----------\n------------------------------")
                print("1. Paquete Turistico economico incluye lo siguiente \n* Hotel 1 Estrellas \n* Desayuno Incluido \n* Vuelo incluido de ida\n------------------------------")
                print("2. Paquete Turistico basico incluye lo siguiente \n* Hotel 3 Estrellas \n* Desayuno, almuerzo y cena incluido \n* Transporte al hotel\n------------------------------")
                print("3. Paquete Turistico Premium incluye lo siguiente \n* Hotel 5 Estrellas \n* Alimentacion Incluida mas bares \n* Vuelos incluidos de ida y vuelta \n* Trasporte al Hotel\n------------------------------")
                print("4. Volver al menú anterior.")
                print("------------------------------")
                
                opcion_p = input("Ingresa una opcion: ")
                print("------------------------------")
                paquete_t.append(opcion_p)

                if opcion_p == '4':
                    break
                elif opcion_p == '1':
                    print ("Usted ha ingresado la opcion 1 Paquete Turistico economico.\n------------------------------")
                    break
                elif opcion_p == '2':
                    print ("Usted ha ingresado la opcion 2 Paquete Turistico Basico.\n------------------------------")
                    break
                elif opcion_p == '3':
                    print ("Usted ha ingresado la opcion 3 Paquete Turistico Premium.\n------------------------------")
                    break
                else:
                    print("Elige nuevamente una opcion que sea correcta.\n------------------------------")
                    
        elif opcion == '2':
            print(f"-----------------------CREA TU PAQUETE!!-----------------------")
            
            nombre_paquete = input("Ingrese un nombre para tu paquete personalizado: ")
            paquete_creado.append(nombre_paquete)
            descripcion = input("Ingrese la Descripcion del paquete: ")
            paquete_creado.append(descripcion)
            adicional = input("Ingrese lo que incluye el paquete (separado por comas): ")
            adicional_paquete.append(adicional)
            lista_adicional = adicional.split(',')
            adicional_paquete.extend(lista_adicional)
            lista_adicional = [item.strip() for item in lista_adicional]
            precio = float(input("Ingrese el precio que tiene el paquete: "))
            paquete_creado.append(precio)

            
            print(f"-----------------------PAQUETE CREADO-----------------------")
            print(f"Nombre del paquete: {paquete_creado[0]}")
            print(f"Descripcion del producto: {paquete_creado[1]}")
            print(f"Precio del paquete: ${paquete_creado[2]} COP")
            print(f"Lo que incluye el paquete:")
            for item in lista_adicional:
                print(f"-{item}")
                
        elif opcion == '3':
            break   
        else:
            print("Eliga una opcion correcta nuevamente.")
            
#------------------------------ RESERVA VUELOS ---------------------------------------

vuelos_reservados = []

def catalogo_vuelos(destino):
  Vuelos_Catalogo = {
    'cartagena':[
      {'clase': 'economico', 'precio':100000},
      {'clase': 'Primera', 'precio':250000, 'Beneficios': 'Comida incluida y Zona VIP'},
      {'clase': 'Privada', 'precio':450000, 'Beneficios': 'Comida incluida, champaña, bar, zona VIP y de entretenimiento'},
      ],
    'medellin':[
      {'clase': 'economico', 'precio':150000},
      {'clase': 'Primera', 'precio':300000, 'Beneficios': 'Comida incluida y Zona VIP'},
      {'clase': 'Privada', 'precio':500000, 'Beneficios': 'Comida incluida, champaña, bar, zona VIP y de entretenimiento'},
      ] ,
    'santa marta':[
      {'clase': 'economico', 'precio':100000},
      {'clase': 'Primera', 'precio':200000, 'Beneficios': 'Comida incluida y Zona VIP'},
      {'clase': 'Privada', 'precio':450000, 'Beneficios': 'Comida incluida, champaña, bar, zona VIP y de entretenimiento'},
      ],
  }
  return Vuelos_Catalogo.get(destino.lower(), [])

def mostrar_vuelos_disponibles(destino):
    catalogo = catalogo_vuelos(destino)
    if catalogo:
        print(f"\nVuelos disponibles para {destino.capitalize()}:")
        for vuelo in catalogo:
            print(f"- Clase: {vuelo['clase'].capitalize()}, Precio: ${vuelo['precio']}")
    else:
        print(f"No hay vuelos disponibles para {destino}.")

def reservar_vuelo():
    # Eliminamos las comas innecesarias en los inputs
    destino = input("Ingrese el destino del vuelo: ").lower()
    mostrar_vuelos_disponibles(destino)

    fecha = input("Ingrese la fecha en la que desea viajar DD/MM/AAAA: ")
    clase_vuelo = input("Ingrese la clase del vuelo que prefiere: ").strip().lower()
    cantidad_asientos = int(input("Ingrese la cantidad de asientos: "))

    # Obtenemos el catálogo de vuelos para el destino
    catalogo = catalogo_vuelos(destino)

    vuelo_reservado = {}

    # Buscamos el vuelo que coincide con la clase seleccionada
    for vuelo in catalogo:
        if vuelo['clase'].lower() == clase_vuelo:
            vuelo_reservado = {
                'destino': destino.capitalize(),
                'fecha': fecha,
                'clase_vuelo': vuelo['clase'],
                'precio': vuelo['precio'],
                'cantidad_asientos': cantidad_asientos,
                'costo_total': vuelo['precio'] * cantidad_asientos
            }
            # Añadimos la reserva al listado de reservas
            vuelos_reservados.append(vuelo_reservado)
            break

    # Si la reserva se realizó correctamente, mostramos los detalles
    if vuelo_reservado:
        print("\n-----------------------------------Información de la Reserva-----------------------------------")
        print(f"Destino: {vuelo_reservado['destino']}")
        print(f"Fecha: {vuelo_reservado['fecha']}")
        print(f"Clase de vuelo: {vuelo_reservado['clase_vuelo']}")
        print(f"Cantidad de asientos: {vuelo_reservado['cantidad_asientos']}")
        print(f"Precio por persona: ${vuelo_reservado['precio']}")
        print(f"Costo total: ${vuelo_reservado['costo_total']}")
    else:
        print("La clase de vuelo seleccionada no está disponible para el destino seleccionado.")


def verificar_vuelo_reservado():

    if vuelos_reservados:
            print("\n-----------------Vuelos Reservados-----------------")
            for i, vuelo in enumerate(vuelos_reservados, 1):
                print(f"\nReserva {i}:")
                print(f"Destino: {vuelo['destino']}")
                print(f"Fecha: {vuelo['fecha']}")
                print(f"Clase de vuelo: {vuelo['clase_vuelo']}")
                print(f"Cantidad de asientos: {vuelo['cantidad_asientos']}")
                print(f"Precio por persona: ${vuelo['precio']}")
                print(f"Costo total: ${vuelo['costo_total']}")
    else:
         print("No tienes ninguna reserva realizada.")

def reserva_v():
    while True:
      print("\n---------------MENÚ PRINCIPAL---------------")
      print("1. Reservar Vuelos")
      print("2. Verificar vuelo reservado")
      print("3. Salir")
      print("---------------------------------------------")

    # Solicita una opción al usuario
      opcion = input("Elija una opción: ")

      if opcion == '1':
        # Llama a la función para reservar vuelo
          reservar_vuelo()
      elif opcion == '2':
        # Llama a la función para verificar vuelos reservados
        verificar_vuelo_reservado()
      elif opcion == '3':
        # Opción para salir del programa
          print("Gracias por su visita. ¡Hasta pronto!")
          break
      else:
        # Si la opción ingresada no es válida, muestra un mensaje de error
          print("Elija una opción correcta nuevamente.")

#-----------------------------------------------RESERVA HOTELES---------------------------------------------------

hoteles_cartagena = [
    ['Hilton: 5 estrellas', [['Habitación individual', 120000], ['Habitación doble', 200000]]],
    ['Sentar: 4 estrellas', [['Habitación individual', 100000], ['Habitación doble', 180000]]]
]

hoteles_santamarta = [
    ['semor: 5 estrellas', [['Habitación individual', 120000], ['Habitación doble', 200000]]],
    ['Sentir: 4 estrellas', [['Habitación individual', 100000], ['Habitación doble', 180000]]]
]

hoteles_medellin=[

    ['luna: 5 estrellas', [['Habitación individual', 120000], ['Habitación doble', 200000]]],
    ['experanza: 4 estrellas', [['Habitación individual', 100000], ['Habitación doble', 180000]]]

]

def reserva_hoteles():
    print("""
 _______________________________
|                               |
|       RESERVA TU HOTEL        |
|_______________________________|

""")
    personas = int(input("¿Cuántas personas se hospedarán?: "))
    noches = int(input("¿Cuántas noches se hospedarán?:  "))



    print("""

 _____________________________________
|                                     |  
|  elija un destino entre:            |
|                                     |  
|  cartagena                          |           
|  santa marta                        |
|  medellin                           |
|_____________________________________|          
 
""")



    destino = input("¿Hacia dónde viaja?:  ").lower()





    if destino == 'cartagena':
        print("""

 _____________________________________
|                                     |  
|  HOTELES DISPONIBLES EN CARTAGENA   |                     
|_____________________________________|    
""")

        for i, hotel in enumerate(hoteles_cartagena):
            print(f"\n{i+1}. {hotel[0]}")


            print("\nHabitaciones disponibles:")
            for j, habitacion in enumerate(hotel[1]):
                print(f"{j+1}. {habitacion[0]}: ${habitacion[1]} por noche")




        hotel_reservado = int(input("\nElija el número del hotel: ")) - 1
        habitacion_elejida = int(input("Elija el número de la habitación: ")) - 1

        hotel_finalmente_reservado = hoteles_cartagena[hotel_reservado]
        habitacion_finalmente_elejida = hotel_finalmente_reservado[1][habitacion_elejida]

        costo_final = habitacion_finalmente_elejida[1] * noches


        print(f""" 
     _____________________________
    |--- Resumen de su reserva ---|
    |_____________________________|
        \nHotel: {hotel_finalmente_reservado[0]}""")

        print(f"Habitación: {habitacion_finalmente_elejida[0]}\nTotal: ${costo_final}")
        confirmacion = input("¿Está seguro de la reserva? (sí/no): ").lower()

        if confirmacion == 'si':
            print('Reserva completada')
        elif confirmacion == 'no':
            print('Reserva cancelada')

    elif destino == 'santa marta':
     

   
        print("""

 _____________________________________
|                                     |  
|  HOTELES DISPONIBLES EN SANTAMARTA  |                     
|_____________________________________|    
""")

        for i, hotel in enumerate(hoteles_santamarta):
            print(f"\n{i+1}. {hotel[0]}")


            print("\nHabitaciones disponibles:")
            for j, habitacion in enumerate(hotel[1]):
                print(f"{j+1}. {habitacion[0]}: ${habitacion[1]} por noche")




        hotel_reservado = int(input("\nElija el número del hotel: ")) - 1
        habitacion_elejida = int(input("Elija el número de la habitación: ")) - 1

        hotel_finalmente_reservado = hoteles_santamarta[hotel_reservado]
        habitacion_finalmente_elejida = hotel_finalmente_reservado[1][habitacion_elejida]

        costo_final = habitacion_finalmente_elejida[1] * noches


        print(f""" 
     _____________________________
    |--- Resumen de su reserva ---|
    |_____________________________|
        \nHotel: {hotel_finalmente_reservado[0]}""")



        print(f"Habitación: {habitacion_finalmente_elejida[0]}\nTotal: ${costo_final}")
        confirmacion = input("¿Está seguro de la reserva? (sí/no): ").lower()

        if confirmacion == 'si':
            print('Reserva completada')
        elif confirmacion == 'no':
            print('Reserva cancelada')

   

    elif destino == "medellin":
        print("""

 _____________________________________
|                                     |  
|  HOTELES DISPONIBLES EN MEDELLIN    |                     
|_____________________________________|    
""")

        for i, hotel in enumerate(hoteles_medellin):
            print(f"\n{i+1}. {hotel[0]}")


            print("\nHabitaciones disponibles:")
            for j, habitacion in enumerate(hotel[1]):
                  print(f"{j+1}. {habitacion[0]}: ${habitacion[1]} por noche")




        hotel_reservado = int(input("\nElija el número del hotel: ")) - 1
        habitacion_elejida = int(input("Elija el número de la habitación: ")) - 1

        hotel_finalmente_reservado = hoteles_santamarta[hotel_reservado]
        habitacion_finalmente_elejida = hotel_finalmente_reservado[1][habitacion_elejida]

        costo_final = habitacion_finalmente_elejida[1] * noches


        print(f""" 
     _____________________________
    |--- Resumen de su reserva ---|
    |_____________________________|
        \nHotel: {hotel_finalmente_reservado[0]}""")



        print(f"Habitación: {habitacion_finalmente_elejida[0]}\nTotal: ${costo_final}")
        confirmacion = input("¿Está seguro de la reserva? (sí/no): ").lower()

        if confirmacion == 'si':
            print('Reserva completada')
        elif confirmacion == 'no':
            print('Reserva cancelada')

    else:
        print("Destino no disponible. Por favor, elija entre 'cartagena' o 'santa marta' o 'medellin'.")

main_menu()


