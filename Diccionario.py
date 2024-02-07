def add_career(carreras):
    carrera = {}
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    carrera['carrera'] = nombre_carrera
    carreras.append(carrera)
    print("Carrera agregada correctamente.")

def show_careers(carreras):
    print("Lista de carreras: ")
    for carrera in carreras:
        print(f"Nombre: {carrera['carrera']}")

def update_career(carreras):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    nuevo_nombre = input("Ingrese el nuevo nombre de la carrera: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            carrera['carrera'] = nuevo_nombre
            print("Carrera actualizada correctamente.")
            return

    print("Carrera no encontrada.")

def delete_career(carreras):
    nombre_eliminar = input("Nombre de la carrera que desea eliminar: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_eliminar:
            carreras.remove(carrera)
            print("Carrera eliminada correctamente.")
            return

    print("Carrera no encontrada.")

def add_classes(carreras):
    nombre_carrera = input("Ingrese el nombre de la carrera para agregar clases: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            nombre_clase = input("Ingrese el nombre de la clase: ")
            if 'clases' not in carrera:
                carrera['clases'] = []
            carrera['clases'].append(nombre_clase)
            print("Clase agregada correctamente.")
            return

    print("Carrera no encontrada.")

def show_classes(carreras):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            if carrera.get('clases'):
                print(f"Clases de la carrera {nombre_carrera}: ")
                for clase in carrera['clases']:
                    print(f" - {clase}")
            else:
                print("No hay clases registradas.")
            return

    print("Carrera no encontrada.")

def update_classes(carreras):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            for i, clase in enumerate(carrera.get('clases', [])):
                nombre_clase = input("Ingrese el nombre de la clase: ")
                if clase == nombre_clase:
                    nuevo_nombre = input("Ingrese el nuevo nombre de la clase: ")
                    carrera['clases'][i] = nuevo_nombre
                    print("Clase actualizada correctamente.")
                    return
                else:
                    print("Clase no encontrada.")
            else:
                print("No hay clases registradas.")
                return

    print("Carrera no encontrada.")

def delete_classes(carreras):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    nombre_eliminar = input("Ingrese el nombre de la clase que desea eliminar: ")

    for carrera in carreras:
        if carrera['carrera'] == nombre_carrera:
            if nombre_eliminar in carrera.get('clases', []):
                carrera['clases'].remove(nombre_eliminar)
                print("Clase eliminada correctamente.")
                return
            else:
                print("Clase no encontrada.")
                return

    print("Carrera no encontrada.")

def main():
    carreras = []

    while True:
        try:
            print("\n------------ Menu ---------------")
            print("1. Agregar carrera")
            print("2. Mostrar carrera")
            print("3. Actualizar carrera")
            print("4. Eliminar carrera")
            print("5. Menu clases")
            print("6. Salir")
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion no valida.")
            continue

        if opcion == 1:
            add_career(carreras)
        elif opcion == 2:
            show_careers(carreras)
        elif opcion == 3:
            update_career(carreras)
        elif opcion == 4:
            delete_career(carreras)
        elif opcion == 5:
            while True:
                try:
                    print("\n------------ Menu clases --------------")
                    print("1. Agregar clases")
                    print("2. Mostrar clases")
                    print("3. Actualizar clases")
                    print("4. Eliminar clases")
                    print("5. Regresar")
                    opcion_clase = int(input("Seleccione una opcion: "))
                except ValueError:
                    print("Opcion no valida.")
                    continue

                if opcion_clase == 1:
                    add_classes(carreras)
                elif opcion_clase == 2:
                    show_classes(carreras)
                elif opcion_clase == 3:
                    update_classes(carreras)
                elif opcion_clase == 4:
                    delete_classes(carreras)
                elif opcion_clase == 5:
                    print("Regresando al menu anterior....")
                    break
                else:
                    print("Opcion no valida.")
        elif opcion == 6:
            print("Saliendo....")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
