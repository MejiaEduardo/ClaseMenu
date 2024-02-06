seguir= True
carreras=[]
Clases=[]

while seguir:
    print("*****Menu*******")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar Carrera")
    print("5. Ingresar clases de las carreras")
    print("6. salir")
    opcion = int (input("Ingrese su opcion:"))
    
    print("*************")
    if opcion==1:
        print("Ingresar carrera")
        nombre = input("Nombre:")
        dicCarrera={}
        dicCarrera["carrera"]= nombre
        carreras.append(dicCarrera)
    elif opcion==2:
        print("**Leer (Mostrar) carrera**")
        for carrera in carreras:
            print("-Nombre:"+carrera["carrera"])
    elif opcion ==3:
        print("Actualizar carrera")
        nombre_carrera = input("Ingrese el nombre de la carrera a actualizar: ")
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == nombre_carrera:
                nueva_carrera = input("Ingrese el nuevo nombre de la carrera: ")
                carrera["carrera"] = nueva_carrera
                print("Carrera actualizada exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("La carrera no fue encontrada.")
    elif opcion==4:
         carreraBorrar = input("Ingrese nombre de la carrera : ")
         indice = 0
         encontrado = False
         for carrera in carreras:
            if carrera["carrera"] == carreraBorrar:
                encontrado = True
                break
            else :
                indice = indice + 1
         if encontrado :
            carreras.remove(carreras[indice])
            print("Elemento borrado")
         else:
            print("No existe")
    elif opcion==5:
        print("****************Menu*************")
        print("1. crear la clase")
        print("2. leer la clase ")
        print("3. Actualizar clase")
        print("4. Borrar  Clase")
        print("5.  volver a el menu principal")
        opclase =int(input ("ingrese una opcion "))
        print("*********************************************")
        if opclase ==1 :
            print("Ingrese la clase ")
            NomClase=input("NomClase")
            dicClase={}
            dicClase["Nombre : "]= NomClase
            Clases.append(dicClase)
        elif opclase==2:
            print ("leer o mostrar Clases")
            for Clase in Clases:
                print("-Nombre:"+Clases["Clase"])
        elif opclase==3:
            print("Actualizar carrera")
            nombre_clase = input("Ingrese el nombre de la carrera a actualizar: ")
            encontrado = False
            for Clases in Clases:
                if Clase["clase"] == nombre_clase:
                    nueva_clase = input("Ingrese el nuevo nombre de la Clase: ")
                    Clase["clase"] = nueva_clase
                    print("Clase actualizada exitosamente.")
                    encontrado = True
                    break
            if not encontrado:
                print("La Clase no fue encontrada.")
        elif opclase==4:
            ClaseBorrar = input("Ingrese nombre de la Clase : ")
        indice = 0
        encontrados = False
        for Clases in Clase:
            if Clases["Clase"] == ClaseBorrar:
                encontrados = True
                break
            else :
                indice = indice + 1

        if encontrados :
            Clases.remove(Clases[indice])
            print("Elemento borrado")
        else:
            print("No existe")
    elif opclase==5:
        print ("Volver al menu principal")     
        print("********************************************")       
    elif opcion==6:
        print("hasta la proxima")
        seguir==False
print("**************")