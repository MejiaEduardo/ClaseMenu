import datetime 
seguir=True  
fechaordenLista=[]  
TipoOrden=[]

Fecha = int(input("ingrese la fecha de que esta: "))    
Cliente = str(input("ingrese el nombre del cliente: "))
Fechaclienteretiro = int(input("ingrese la fecha para su retiro: "))
fechainicioreparacion= int(input("Ingrese la fecha en que se realizo la primera reparación: "))
  
fechaordenLista.append(Fecha) 
fechaordenLista.append(Cliente)
fechaordenLista.append(Fechaclienteretiro)


while seguir:
    print("******Tipo de orden***********")
    print("1.ingrese una orden normal")
    print("2.ingrese una orden de garantia")
    print("3. Actualizar una orden")
    print("4. Borrar una orden") 
    print("5.salir")
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion==1:
        print("Orden Normal y este tendra un costo")
        str(input("ingrese el costo de la orden"))
        TipoOrden.append(1)      
        total=float(input("Digite el costo de la reparacion: $"))       
        total=0
        print("el costo de la reparacion es : ",total+".00")   
        
    elif opcion==2: 
        print("Esta es una Orden de Garantia, por lo tanto no tiene costo.")
        str(input("Ingrese el detalle de la orden"))
        TipoOrden.append(2) 
        if  confirirmar_garantia == True :
            for confirirmar_garantia in  range(len(diastotales)):
                diasretardo=(datetime.date.today()- datetime.date(Fecha)).days
            if diasretardo<0:
                print("la fecha de inicio de la reparacion debe ser mayor a hoy")
            elif Fecha > datetime.date.today():
                print ("el numero de dia ingresado es superior al actual, vuelva a intentarlo")
            else:
                diastotales= (Fechaclienteretiro - Fecha)/datetime.timedelta(days=1)
                print(f"\nCuenta con {diastotales} día(s) para recibir su producto.\n")

            if diastotales<=15:
                print(f"Tiene ")
            else:
                print("\n\nUsted ha retrasado la entrega del producto,\ndebido a esto le cobramos una multa de $500")
                total+=500
                print(f"Por lo tanto su total a pagar es de ${total+500}")  
                print("\nLa garantia se encuentra activa\n")
            confirirmar_garantia==False
            print("\nLa garantia esta vencida\n")
    elif opcion==3:
        Tipo_Orden = input("Ingrese el Tipo de Orden que desea Actualzar: ")
        for TipoOrden in TipoOrden:
         if  TipoOrden['Orden'] == Tipo_Orden:
            for i, TipoOrden in enumerate(TipoOrden.get('Orden', [])):
                Tipo_Orden = input("Ingrese el Nuevo Tipo de orden que desea : ")
                if TipoOrden == Tipo_Orden:
                    TipoOrden['Orden'][i] = Tipo_Orden
                    print("Orden Actualizada correctamente.")
                    break
                else:
                    print("Orden no encontrada.")
                    break
    elif  opcion == 4:
        print("Vamos a borrar una orden")
        numorden = int(input("Digite el numero de la orden que desea eliminar"))
        for TipoOrden in  TipoOrden:
            if TipoOrden in numorden.get('Orden', []):
                numorden['Orden'].remove(TipoOrden)
                print("Orden eliminada correctamente.")
                break
            else:
                print("orden no encontrada.")
                break

        print("Orden no encontrada.")
            
    elif opcion==5 :
        print("hasta la proxima")
        seguir==False
print("***********************************************")

