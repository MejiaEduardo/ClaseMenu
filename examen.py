
Clientes=[]

def InfoCliente():
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
    
    
def visualizar_contrato(contrato):
    print("Empleador: ", contrato["empleador"])
    print("Cantidad de metros cuadrados: ", contrato["metros"])
    print("Cliente: ", contrato["cliente"])
    print("Identidad: ", contrato["identidad"])
    print("Precio: ", contrato["precio"])
    print("Estado: ", contrato["estado"])
    print()

#Definicion de funciones para agregar y mostrar los datos del cliente y del contrato
agregarCliente=InfoCliente
mostrarCliente=lambda Id: Clientes[Id]


#Se agrego un nuevo contrato con un empleado y una cantidad de metros

menu = ["+++++++ Menu +++++++",
        "1. Ingresar un contrato",
        "2. Mostrar Contrato",
        "3. Buscar el contrato",
        "4. Salir"]


menuOrderTypes = ["Ingrese tipo de Contrato :",
                  "1. En Espera",
                  "2. En Proceso",
                  "3. Finalizado",
                  "4. Cambiar el estado del Contrato"
                  "5. Ingrese cualquier numero o letra para SALIR"]


def makeMenu(menu, start, end):
    for item in menu:
        print(item)
    try:
        option = int(input("Ingrese la opción: "))
    except:
        return 0
    else:
        if option >= start and option <= end:
            return option
        else:
            return 0


    
#Preguntas y respuestas para obtener información del contrato.
print("Ingrese la informacion del nuevo contrato.")
nombreEmpleado = input ("Nombre del Empleado: ")
metrosTrabajados = int(input("¿Cuántos metros trabajó?: "))
nombreCliente=input("Nombre del Cliente: ")
IDcliente=int(input("escriba el id del Cliente: "))
presioContrato=int(input("Ingrese el precio de su contrato: "))









#Mostrar todos los contratos en una tabla.
print("\n\tTabla de Contratos")
print("----------------------------")
print("---------------------------")
print ("| Nombre | Metros Trabajados |")
print ("------------------------------")

