"""

ingresar valores usando diccionarios y arreglos
arreglo de comida
1. ingresar plato(nombre, tipo,)
2. ingresar ingredientes: usamos un while si pone salir se sale
buscar comida
pide nombre, cantidad, unidad, costo.
3. Ingresar receta
buscar comida
while para que vaya ingresando pasos
si pone salir se sale
4. Listado de alimentos
5. Listado especifico
busca comida
6. salir

"""
comida = []
opcion = 0
seguir = True

while seguir:
    try:
        print("********MENU**********")
        print("1. Ingresar una comida")
        print("2. Ingresar Ingredientes")
        print("3. Ingresar receta")
        print("4. Ver lista de comidas")
        print("5. Buscar comida")
        print("6. Salir")
        opcion = int(input("Ingresa una opcion: "))
    except:
        print("***** Valor ingresado no valido ******")
    else:
        match opcion:
            case 1:
                nvacomida = {}
                nvacomida['Nombre'] = input("Ingresar nombre de la comida: ")
                nvacomida['Tipo'] = input("Ingresar el tipo de comida: ")
                comida.append(nvacomida)
                print("Alimento ingresado correctamente")
            case 2:
                ingredientes = []
                nvoingrediente = {}
                continuar = False
                print(" Agregar ingredientes ")
                busq_comida = input("Que comida desea ingresar ingredientes: ")
                indice = 0
                for listado in comida:
                    if busq_comida == listado['Nombre']:
                        continuar = True
                    if not continuar:
                        indice += 1
                if not continuar:
                    print("**** Comida no econtrada ****")
                else:

                    ingresar = True

                    while ingresar:
                        nvoingrediente['Nombre'] = input("Ingresa nombre de ingrediente (Salir para salir)")
                        if nvoingrediente['Nombre'] == "Salir":
                            ingresar = False
                            continue;

                        try:
                            nvoingrediente['Cantidad'] = float(input("Ingresa la cantidad de ingrediente"))
                            nvoingrediente['Unidad'] = input("Ingresa la unidad de los ingrediente ")
                            nvoingrediente['Costo'] = float(input("Ingresa el costo del ingrediente "))
                            ingredientes.append(nvoingrediente)
                        except:
                            print("Valor ingresado no valido")
                        else:
                            print("Ingrediente agregado correctamente")
                            comida[indice]['Ingredientes'] = ingredientes
            case 3:
                print("Argegar ingrediente: ")
                busq_comida = input("Que comida va a usar: ") 
                receta = []
                contador_re = 0
                econtrado = False
                for listado in comida:
                    if busq_comida == listado['Nombre']:
                        econtrado = True
                    if not econtrado:
                        contador_re += 1
                if not econtrado:
                    print("No se encontro la comida")
                    continue;
            
                ingresar = True
                while ingresar:
                    descripcion = input("Ingrese la descripcion: ")

                    if descripcion == "Salir":
                        ingresar = False
                        continue;
                    else:
                        receta.append(descripcion)
                
                comida[contador_re]['Receta'] = receta
            case 4:
                print(f"***** comidas ingresadas: {len(comida)}")
                for listado in comida:
                    print(f"{str(comida.index(listado) + 1)} ) {listado}")
            case 5:
                print(" Busqueda de comida")
                buscar_comida = input("Que comida desea buscar")

                for listado in comida:
                    if buscar_comida == listado['Nombre']:
                        print("Se encontro esta comida: ")
                        print(listado)
                    else:
                        print("No se encontro la comida")
            case 6:
                seguir = False
