from datetime import datetime

def menuPrincipal(menu, inicio, fin):
    for seleccion in menu:
        print(seleccion)
    try:
        opcion=int(input("Seleccione una opcion: "))
    except:
        return 0
    else:
        if opcion >=inicio and opcion <=fin:
            return opcion
        else:
            return 0
            
def obtenerFecha(etiqueta):
    while (True):
        try:
            fecha= datetime.strptime(input(etiqueta), "%y-%m-%d")
            return fecha
        except:
            print("Ingrese una opcion correcta en el formato YYYY-MM-DD ")

def nombreEmpleado(etiqueta):
     while (True):
        nombre=input(etiqueta)
        try:
            isFloat=float(nombre)
            print("Por favor ingrese un nombre correcto")
        except:
            try:
                isInt=int(nombre)
                print("Por favor ingrese un nombre correcto")
            except:
                    if nombre.replace('.','.').isdigit():
                        print("Por favor ingrese un nombre correcto")
                    else:    
                        return nombre
                    
        
def nombreCliente(etiqueta):
    while (True):
        nombre=input(etiqueta)
        try:
            float(nombre)
            print("Por favor ingrese un nombre correcto")
        except:
            try:
                int(nombre)
                print("Por favor ingrese un nombre correcto")
            except:
                    if nombre.replace('.','.').isdigit():
                        print("Por favor ingrese un nombre correcto")
                    else:      
                        return nombre
            
def idCliente(etiqueta):
    while (True):
        try:
            id=input(etiqueta)
            return id
        except:
            print("Ingrese el ID correcto")

def precioContrato(etiqueta):
    while (True):
        try:
            precio=float(input(etiqueta))
            return precio
        except:
            print("Ingrese una cantidad correcta")
            
def obtenerMetros(etiqueta):
    while (True):
        try:
            metros=float(input(etiqueta))
            return metros
        except:
            print("Ingrese una cantidad correcta")
    
def obtenerEstado(etiqueta):
    while (True):
        try:
            palabraspermitidas = ['espera', 'proceso', 'finalizado']
            print("--espera--proceso--finalizado")
            estado=input(etiqueta)
            if estado.lower() in palabraspermitidas:
                return estado
            else:
                raise ValueError("Ingrese un estado correcto")
        
        except ValueError as e:
            print(e)