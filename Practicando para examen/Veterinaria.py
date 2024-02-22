"""
ingresar mascotas con nombre, tipo, descripcion.
atendidas por orden de llegada
menu con ciclo infinito while
1. ingresar ,ascota
2. ver listado completo de mascotas
3. atender mascota
4. salir
"""
mascotas = []
opcion = 0
contador = 0
seguir = True

while seguir:
    try:
        print("*** MENU ***")
        print ("1. Ingresar nueva mascota")
        print("2. Ver listado completo de mascotas")
        print("3. Atender siguientes mascota")
        print("4. Salir")
        opcion = int(input("Ingresa un opcion:"))
    except:
        print(" OPCION INGRESADA NO VALIDA")
    else:
        match opcion:
            case 1:
                nvamascota = {}
                nvamascota['Nombre'] = input("Ingresa el nombre de la mascota: ")
                nvamascota['Tipo'] = input("Ingresa el nombre de la mascota: ")
                nvamascota['Descripcion'] = input("Ingresa el nombre de la mascota: ")
                mascotas.append(nvamascota)
                print(" *** Ingresado correctamente *** \n")
            case 2:
                if len(mascotas) > 0:
                    print(f"********* Cantidad de mascotas: {len(mascotas)} *********")
                    for listado in mascotas:
                        print(f"{str(mascotas.index(listado) + 1 )} ) {listado}")
                else:
                    print("*** No hay ninguna mascota ingresada ***")
            case 3:    
                if (len(mascotas) > 0 and contador < len(mascotas)):
                    print(f" Siguiente mascota a atender: {mascotas[contador]}")
                    contador += 1
                else:
                    print(" ***** No hay mascotas para atender ******")
            case 4:
                seguir = False
            case defaul:
                print("OPCION INGRESADA NO VALIDA")