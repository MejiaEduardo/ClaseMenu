"""
función para crear un contrato. Solicita al usuario los datos del contrato y ver que se ingresen correctamente.
Devuelve un diccionario con los datos del contrato.
"""
def crear_contrato():
    try:
        empleador = input("Ingrese el empleador responsable: ")
        metros = int(input("Ingrese la cantidad de metros cuadrados a realizar el aseo: "))    
        cliente = input("Ingrese nombre completo del cliente: ")
        identidad = input("Ingrese la identidad del cliente: ")
        precio = float(input("Ingrese el precio por el cual se realiza el contrato: "))
        estado = input("Ingrese el estado del contrato (en espera, en proceso, finalizado): ")
        while estado not in ["en espera", "en proceso", "finalizado"]:
            estado = input("Estado inválido. Ingrese el estado del contrato (en espera, en proceso, finalizado): ")
        contrato = {"empleador": empleador, "metros": metros, "cliente": cliente, "identidad": identidad, "precio": precio, "estado": estado}
        return contrato
    except ValueError as e:
        print("Error: Debes ingresar un valor numérico válido.")
        return None

"""
función para mostrar los datos de un contrato. Recibe como parámetro un diccionario con los datos del contrato y muestra 
cada dato en una línea separada.
"""
def visualizar_contrato(contrato):
    print("Empleador: ", contrato["empleador"])
    print("Cantidad de metros cuadrados: ", contrato["metros"])
    print("Cliente: ", contrato["cliente"])
    print("Identidad: ", contrato["identidad"])
    print("Precio: ", contrato["precio"])
    print("Estado: ", contrato["estado"])
    print()

"""
función para mostrar todos los contratos almacenados en una lista. Recorre la lista y por cada elemento (contrato), 
llama a la función visualizar_contrato()
"""
def visualizar_todos_contratos(contratos):
    for contrato in contratos:
        visualizar_contrato(contrato)


"""
función para buscar contratos con un estado específico. Recibe como parámetros una lista de contratos y un estado. 
Recorre la lista y verifica si el estado de cada contrato coincide con el estado buscado. Si coincide, agrega el contrato a una lista 
auxiliar y devuelve esta lista al final.
"""
def buscar_contratos_por_estado(contratos, estado):
    contratos_encontrados = []
    for contrato in contratos:
        if contrato["estado"] == estado:
            contratos_encontrados.append(contrato)
    return contratos_encontrados

"""
función para cambiar el estado de un contrato. Recibe como parámetros un contrato y un nuevo estado. Verifica que el nuevo estado sea válido y, si lo es,
cambia el estado del contrato y muestra un mensaje indicando que se ha cambiado el estado.
"""
def cambiar_estado_contrato(contrato, nuevo_estado):
    while nuevo_estado not in ["en espera", "en proceso", "finalizado"]:
        nuevo_estado = input("Estado inválido. Ingrese el nuevo estado del contrato (en espera, en proceso, finalizado): ")
    contrato["estado"] = nuevo_estado
    print(f"El estado del contrato ha sido cambiado a {nuevo_estado}.")


"""
función principal del programa. Muestra un menú de opciones al usuario y permite crear, visualizar, buscar y modificar contratos. 
También permite salir del programa.
"""
def main():
    contratos = []
    while True:
        print("\n**************************MENU PRINCIPAL****************************")
        print("1. Crear contrato")
        print("2. Visualizar contrato")
        print("3. Visualizar todos los contratos")
        print("4. Buscar contratos por estado")
        print("5. Cambiar estado de contrato")
        print("6. Salir")
        opcion = int(input("Ingrese la opción deseada:"))
        if opcion == 1:
            contrato = crear_contrato()
            contratos.append(contrato)
        elif opcion == 2:
            if len(contratos) == 0:
                print("No hay contratos ingresados.")
            else:
                identidad = input("Ingrese la identidad del cliente:")
                contrato_encontrado  = None
                for contrato in contratos:
                    if contrato["identidad"] == identidad:
                        contrato_encontrado = contrato
                        break
                if contrato_encontrado is None:
                    print("No se encontro ningun contrato con esta identidad")
                else:
                    visualizar_contrato(contrato_encontrado)
        elif opcion == 3:
            visualizar_todos_contratos(contratos)
        elif opcion == 4:
            estado = input("Ingrese el estado del contrato a buscar: ")
            contratos_encontrados = buscar_contratos_por_estado(contratos, estado)
            if len(contratos_encontrados) == 0:
                print("No se encontraron contratos con el estado especificado.")
            else:
                print("Contratos encontrados:")
                for contrato in contratos_encontrados:
                    visualizar_contrato(contrato)
        elif opcion == 5:
            if len(contratos) == 0:
                print("No hay contratos ingresados.")
            else:
                identidad_cliente = input("Ingrese la identidad del cliente:")
                contrato_encontrado = None
                for contrato in contratos:
                    if contrato["identidad"] == identidad_cliente:
                        contrato_encontrado = contrato
                        break
                if contrato_encontrado is None:
                    print("No se encontro nigun contrato con la identidad ingresada")
                else:
                    nuevo_estado = input("Ingrese el nuevo estado del contrato (en espera, en proceso, finalizado):")
                    while nuevo_estado not in ["en espera", "en proceso", "finalizado"]:
                        nuevo_estado = input("Estado inválido. Ingrese el nuevo estado del contrato (en espera, en proceso, finalizado): ")
                    contrato_encontrado["estado"] = nuevo_estado
                    print(f"El estado del contrato con identidad {identidad_cliente} ha sido cambiado a {nuevo_estado}.")

        elif opcion == 6:
            print("Sale bye :b")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()