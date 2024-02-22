
contratos=[]
Clientes=[]

def infoContrato (empleado,cantidadMetros):
    contrato=[]  
    new_contract = { 'Empleado': empleado ,'Cuantos Metros': cantidadMetros }
    contrato.append(new_contract)


def InfoCliente(cliente,id,Precio):
    ClienteContrato={}
    ClienteContrato['Nombre']=cliente
    ClienteContrato['ID']= id  
    ClienteContrato["PRECIO"]=Precio
    Clientes[len(Clientes)]=ClienteContrato  #Agrega el cliente a la lista de clientes
    
#Definicion de funciones para agregar y mostrar los datos del cliente y del contrato
agregarCliente=InfoCliente
mostrarCliente=lambda Id: Clientes[Id]
mostrarContrato=lambda Empleado: [contratos for contratos in contratos if contratos["Empleado"]==Empleado][0]

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
infoContrato((nombreEmpleado).strip(),metrosTrabajados)









#Mostrar todos los contratos en una tabla.
print("\n\tTabla de Contratos")
print("----------------------------")
print("---------------------------")
print ("| Nombre | Metros Trabajados |")
print ("------------------------------")
for contrato in contratos :
    print ("| %10s | %25d |"%(contrato['Empleado'],contrato ['Cuantos Metros']))
print("------------------------------")

#Buscar un contrato por nombre del empleado.    

