import datetime 
seguir=True  
fechaordenLista=[]  

Fecha = int(input("ingrese la fecha de que esta: "))    
Cliente = str(input("ingrese el nombre del cliente: "))
Fechaclienteretiro = int(input("ingrese la fecha para su retiro: "))
fechainicioreparacion= int(input("Ingrese la fecha en que se realizo la primera reparación: "))
#se agregan las fechas a una lista  
fechaordenLista.append(Fecha) 
fechaordenLista.append(Cliente)
fechaordenLista.append(Fechaclienteretiro)


while seguir:
    print("******Tipo de orden***********")
    print("1.ingrese una orden normal")
    print("2.ingrese una orden de garantia") 
    print("3.salir")
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion==1:
        print("Orden Normal y este tendra un costo")
        
    elif opcion==2: 
        print("Esta es una Orden de Garantia, por lo tanto no tiene costo.")
    elif opcion==3 :
        print("hasta la proxima")
        seguir==False
print("***********************************************")
print(f"La fecha de la orden fue {fechaordenLista[0]}")
print(f"El Cliente es {fechaordenLista[1]}\n")
if opcion == 1:
    total=float(input("Digite el costo de la reparacion: $"))
else:       
    total=0

diasretardo=(datetime.date.today()- datetime.date(fechainicioreparacion)).days

if diasretardo<0:
    print("la fecha de inicio de la reparacion debe ser mayor a hoy")
elif Fecha > datetime.date.today():
    print ("el numero de dia ingresado es superior al actual, vuelva a intentarlo")
else:
    #calculando los días entre la fecha de la orden y la fecha de entrega
    diastotales= (Fechaclienteretiro - Fecha)/datetime.timedelta(days=1)
    print(f"\nCuenta con {diastotales} día(s) para recibir su producto.\n")

    #si supera los 5 días se cobrará un multa de $500
    if diastotales<=5:
        print(f"Su total a pagar es de ${total}")
    else:
        print("\n\nUsted ha retrasado la entrega del producto,\ndebido a esto le cobramos una multa de $500")
        total+=500
        print(f"Por lo tanto su total a pagar es de ${total+500}")  
    

    