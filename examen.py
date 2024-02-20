
contratos=[]

def infoContrato (empleado,cantidadMetros):
    contrato=[new_contract]  
    new_contract = { 'Empleado': empleado ,'Cuantos Metros': cantidadMetros }
    contrato.append(new_contract)


def InfoCliente(cliente,id,Precio):
    ClienteContrato={}
    print(input("Ingrese el nombre del Cliente"))
    print(int("ingrese el id del cliente"))
    print(int("ingrese el precio total del contrato"))

menu = ["+++++++ Menu +++++++",
        "1. Ingresar una orden",
        "2. Mostrar Contrato",
        "3. Buscar el contrato",
        "4. Salir"]


menuOrderTypes = ["Ingrese tipo de Contrato :",
                  "1. En Espera",
                  "2. En Proceso",
                  "3. Finalizado",
                  "3. Ingrese cualquier numero o letra para SALIR"]


    
#Preguntas y respuestas para obtener información del contrato.
print("Ingrese la informacion del nuevo contrato.")
nombreEmpleado = input ("Nombre del Empleado: ")
metrosTrabajados = int(input("¿Cuántos metros trabajó?: "))
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

