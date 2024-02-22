"""

1. ingresar prodcutos: codigo, nombre, precio, costo, inventario
2. mostrar todos los productos (Solo imprimir los productos)
3. mostrar un producto hacer busqueda por nombre
4. Ingresar al inventario (buscar por nombre)
5. sacar  del inventario (buscar por nombre)
6. Salir

"""

def actualizar_invetntario(accion):
    print(f" {accion} del inventario")
    cantidad = 0

    nombre_producto = input("Ingrese el nombre del producto: ")
    indice = 0
    mostrado = False

    for listado in productos:
        if nombre_producto == listado['Nombre']:
            print(listado)
            mostrado = True
        
        if not mostrado:
            indice += 1

    if not mostrado:
        print("***** Valor no encontrado ******")
    else:
        try:
            cantidad = float(input("Ingrese la cantidad: "))
        except:
            print(" Valor ingresado no valido ")
        else:
            if accion == "Ingresar" :
                productos[indice]['Inventario'] += cantidad
            else:
                productos[indice]['Inventario'] -= cantidad
        print("Valor ingresado")

productos = []
opcion = 0
contador = 0
continuar = True

while continuar:
    try:
        print("******** MENU ********")
        print("1. Ingresar un producto")
        print("2. Mostrar todos los productos")
        print("3. Mostrar un producto")
        print("4. Ingresar al inventario")
        print("5. Quitar del inventario")
        print("6. Salir")
        opcion = int(input("Ingresa una opcion: "))
    except:
        print(" ****** VALOR INVALIDO ******")
    else:
        match opcion:
            case 1:
                nvoproductos = {}
                nvoproductos['Codigo'] = input(" Ingresar codigo del producto ")
                nvoproductos['Nombre'] = input(" Ingresar nombre del producto ")
                nvoproductos['Precio'] = float(input(" Ingresar precio del producto "))
                nvoproductos['Costo'] = float(input(" Ingresar costo del producto "))
                nvoproductos['Inventario'] = float(input(" Ingresar inventario del producto "))
                productos.append(nvoproductos)
            case 2:
                if len(productos) > 0 :
                    print (f" ***** Productos ingresados: {len(productos)} ***** ")
                    for listado in productos:
                        print(f" {str(productos.index(listado) +  1)} ) {listado}")
                else:
                    print("***** No hay productos ingresados ******")
            case 3:
                busq_prodcuto = input("Que productos desea buscar (Ingresa su nombre): ")
                for buscar in productos:
                    if busq_prodcuto == buscar['Nombre']:
                        print(buscar)
                else:
                    print("No se encontro el producto")
            case 4:
                actualizar_invetntario("Ingresar")
            case 5:
                actualizar_invetntario("Eliminar")
            case 6:
                continuar = False        