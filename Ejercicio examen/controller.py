import util
from util import  obtenerFecha, obtenerMetros, nombreCliente, nombreEmpleado, precioContrato, idCliente, obtenerEstado
from params import menu
from datetime import datetime, timedelta


def obtenerMenu():
    return util.menuPrincipal(menu, 1,6)
    
def agregar(contratos):
    contrato={}
    contrato["Nombre Empleado"]=nombreEmpleado("Ingrese el nombre del empleado responsable: ")
    contrato["Nombre Cliente"]=nombreCliente("ingrese el nombre del cliente: ")
    contrato["ID Cliente"]=idCliente("Ingrese el ID del cliente: ")
    contrato["Cantidad Metros^2"]=obtenerMetros("Ingrese los metros cuadrados a limpiar:")
    contrato["Precio"]=precioContrato("Ingrese el precio del contrato: ")
    contrato["Estado"]=obtenerEstado("Ingrese el estado del contrato: ")
    contratos.append(contrato)
    print(contratos)
    
def mostrarContrato(contratos):
    nomcliente=nombreCliente("ingrese el nombre del cliente: ")
    for contrato in contratos:
        if contrato["Nombre Cliente"]==nomcliente:
            print(contrato)
        else:
         print("El cliente no se encuentra registrado")
        
def mostrarContratos(contratos):
    print(contratos)
    
def buscarEstado(contratos):
    buscar=obtenerEstado("Ingrese el estado de los contratos que desea buscar: ")
    for  contrato in contratos:
        if contrato["Estado"]==buscar:
            print(contrato)
            break
        else:
            print("El estado no existe")
        
       
def modificarContrato(contratos):
    cliente=nombreCliente("ingrese el nombre del cliente: ")
    for contrato in contratos:
        if contrato["Nombre Cliente"]==cliente:
            newEstado=obtenerEstado("Ingrese el nuevo estado: ")
            if contrato["Estado"]!=newEstado:
                contrato["Estado"]=newEstado
                print(contrato)
                break
            else:
                print("El estado actual es igual al nuevo estado")
        else:
            print("El cliente no se encuentra registrado")
