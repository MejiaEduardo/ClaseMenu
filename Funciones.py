carreras = []
seguir = True

while(seguir):
    try:
        print("\n------------ Menu ---------------")
        print("1. Agregar carrera")
        print("2. Mostrar carrera")
        print("3. Actualizar carrera")
        print("4. Eliminar carrera")
        print("5. Menu clases")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida.")
    else:
        match(opcion):
            case 1:
                carrera = {}
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                carrera['carrera'] = nombre_carrera
                carreras.append(carrera)
                print("Carrera agregada correctamente.")
            case 2:
                print("Lista de carreras: ")
                for carrera in carreras:
                    print(f"Nombre: " + carrera['carrera'])
            case 3:
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                nuevo_nombre = input("Ingrese el nuevo nombre de la carrera: ")

                for carrera in carreras:
                    if carrera['carrera'] == nombre_carrera:
                        carrera['carrera'] = nuevo_nombre
                        print("Carrera actualizada correctamente.")
            case 4:
                nombre_eliminar = input("Nombre de la carrera que desea eliminar: ")

                encontrado = False
                indice = 0
                for carrera in carreras:
                    if carrera['carrera'] == nombre_eliminar:
                        encontrado = True
                        break
                    else:
                        indice += 1
                if encontrado:
                    carreras.remove(carreras[indice])
                else:
                    print("Carrera no encontrada.")
            case 5:
                seguir_clase = True
                while(seguir_clase):
                    try:
                        print("\n------------ Menu clases --------------")
                        print("1. Agregar clases")
                        print("2. Mostrar clases")
                        print("3. Actualizar clases")
                        print("4. Eliminar clases")
                        print("5. Regresar")
                        opcion_clase = int(input("Seleccione una opcion: "))
                    except:
                        print("Opcion no valida.")
                    else:
                        match(opcion_clase):
                            case 1:
                                nombre_carrera = input("Ingrese el nombre de la carrera para agregar clases: ")
                                
                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        nombre_clase = input("Ingrese el nombre de la clase: ")
                                        if 'clases' not in carrera:
                                            carrera['clases'] = []
                                        carrera['clases'].append(nombre_clase)
                                        print("Clase agregada correctamente.")
                                        break
                                    else:
                                        print("Error al agregar clase")
                                else:
                                    print("Carrera no encontrada.")
                            case 2:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")

                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        if carrera['clases']:
                                            print(f"Clases de la carrera {nombre_carrera}: ")
                                            for clase in carrera['clases']:
                                                print(f" - {clase}")
                                        else:
                                            print("No hay clases registradas.")
                                        break
                                else:
                                    print("Carrera no encontrada.")
                            case 3:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")

                                for carrera in carreras:
                                    if carrera['carrera'] == nombre_carrera:
                                        for i, clase in enumerate(carrera['clases']):
                                            nombre_clase = input("Ingrese el nombre de la clase: ")
                                            if clase == nombre_clase:
                                                nuevo_nombre = input("Ingrese el nuevo nombre de la clase: ")
                                                carrera['clases'][i] = nuevo_nombre
                                                print("Carrera modificada correctamente.")
                                                break
                                            else:
                                                print("Clase no encontrado.")
                                    else:
                                        print("Carrera no encontrada.")
                            case 4:
                                nombre_carrera = input("Ingrese el nombre de la carrera: ")                             # for carrera in carreras:
                                print()                                                                                 #     if carrera['carrera'] == nombre_carrera:
                                for carrera in carreras:                                                                #         for i, clase in enumerate(carrera['clases']):
                                    if carrera['carrera'] == nombre_carrera:                                            #             nombre_eliminar = input("Ingrese el nombre de la clase que desea eliminar: ")
                                        nombre_eliminar = input("Ingrese el nombre de la clase que desea eliminar: ")   #             if clase == nombre_eliminar:
                                        if nombre_eliminar in carrera['clases']:                                        #                 carrera['clases'].pop(i)
                                            carrera['clases'].remove(nombre_eliminar)                                   #                 print("Clase borrada correctamente.")
                                            print("Clase eliminada correctamente.")                                     #                 break
                                            break                                                                       #         else:
                                        else:                                                                           #             print("Clase no encontrada.")
                                            print("Clase no encontrada.")                                               #         break
                                    else:                                                                               # else:
                                        print("Carrera no encontrada.")                                                 #     print("Carrera no encontrada.")                                                      
                            case 5:
                                print("Regresando al menu anterior....")
                                seguir_clase = False
                            case default:
                                print("Opcion no valida.")
            case 6:
                print("Saliendo....")
                seguir = False