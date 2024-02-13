import datetime
ordenes=[]

seguir = True

def agregarorden(fecha, cliente, tipo, precio=None, referencia=None):
    nuevaOrden={
        "fecha": fecha,
        "cliente": cliente,
        "tipo": tipo
    }

    if tipo=="1":
        nuevaOrden["precio"]=precio
    elif tipo=="2":
        nuevaOrden["referencia"]


    ordenes.append(nuevaOrden)
    print("Orden agregada exitosamente")

def buscarcliente(cliente):
    return [orden for orden in ordenes if orden ["cliente"]==cliente]

def actualizarorden(orden, NuevaFecha):
    orden["fecha"]= NuevaFecha
    print("Orden Actualizada exitosamente")

def mostrarorden():
    for orden in ordenes:
        print(orden)
        print(f"Fecha: {orden['fecha']}, Cliente: {orden['cliente']}, Tipo: {orden['tipo']}")

def eliminarorden(orden):
    ordenes.remove(orden)
    print("Orden eliminada exitosamente.")

while True:
    print("\n--------------MENU-------------")
    print("1. Ingresar una orden")
    print("2. Mostrar todas las órdenes")
    print("3. Actualizar una orden")
    print("4. Eliminar una orden")
    print("5. Salir")

    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        fecha_orden = input("Ingrese la fecha de la orden: ")
        cliente_orden = input("Ingrese el nombre del cliente: ")
        tipo_orden = input("Ingrese el tipo de orden (1.normal o 2.garantia): ")

        if tipo_orden == "1":
            precio_orden = float(input("Ingrese el precio de la orden normal: "))
            agregarorden(fecha_orden, cliente_orden, tipo_orden, precio=precio_orden)
        elif tipo_orden == "2":
            referencia_orden = input("Ingrese la referencia para la orden de garantía: ")
            agregarorden(fecha_orden, cliente_orden, tipo_orden, referencia=referencia_orden)
        else:
            print("Opción no válida.")
            continue

    elif opcion == 2:
        mostrarorden()

    elif opcion == 3:
        cliente_a_actualizar = input("Ingrese el nombre del cliente para actualizar la orden: ")
        ordenes_cliente = buscarcliente(cliente_a_actualizar)

        if not ordenes_cliente:
            print(f"No se encontraron órdenes para el cliente {cliente_a_actualizar}.")
            continue

        nueva_fecha = input("Ingrese la nueva fecha: ")
        for orden in ordenes_cliente:
            actualizarorden(orden, nueva_fecha)

            
    elif opcion == 4:
        mostrarorden()
        cliente_a_eliminar = input("Ingrese el nombre del cliente para eliminar la orden: ")
        ordenes_cliente = buscarcliente(cliente_a_eliminar)

        if not ordenes_cliente:
            print(f"No se encontraron órdenes para el cliente {cliente_a_eliminar}.")
            continue

        for orden in ordenes_cliente:
            eliminarorden(orden)

    elif opcion == 5:
        print(" Hasta luego.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")