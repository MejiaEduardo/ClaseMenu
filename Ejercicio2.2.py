from abc import ABC, abstractmethod

class Ingrediente:
    def __init__(self, nombre, unidad_medida, costo_por_unidad):
        self.nombre = nombre
        self.unidad_medida = unidad_medida
        self.costo_por_unidad = costo_por_unidad

class Receta(ABC):
    @abstractmethod
    def mostrar_receta(self):
        pass

class RecetaTextual(Receta):
    def __init__(self, pasos, descripciones):
        self.pasos = pasos
        self.descripciones = descripciones

    def mostrar_receta(self):
        for paso, descripcion in zip(self.pasos, self.descripciones):
            print(f"Paso {paso}: {descripcion}")

class ComidaBase(ABC):
    def __init__(self, nombre, tipo_plato):
        self.nombre = nombre
        self.tipo_plato = tipo_plato
        self.ingredientes = []
        self.receta = None

    @abstractmethod
    def mostrar_comida(self):
        pass

class ComidaTextual(ComidaBase):
    def mostrar_comida(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo de plato: {self.tipo_plato}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"{ingrediente.nombre} - {ingrediente.unidad_medida} - {ingrediente.costo_por_unidad}")
        print("Receta:")
        self.receta.mostrar_receta()

def mostrar_listado_comidas(comidas):
    for comida in comidas:
        print(f"{comida.nombre} - {comida.tipo_plato}")

def ingresar_comida():
    nombre = input("Ingrese el nombre del plato: ")
    tipo_plato = input("Ingrese el tipo de plato (ensalada, carnes, hamburguesas): ")
    ingredientes = []
    while True:
        ingrediente_nombre = input("Ingrese el nombre del ingrediente (o 'fin' para terminar): ")
        if ingrediente_nombre.lower() == 'fin':
            break
        ingrediente_unidad_medida = input("Ingrese la unidad de medida: ")
        ingrediente_costo_por_unidad = float(input("Ingrese el costo por unidad de medida: "))
        ingrediente = Ingrediente(ingrediente_nombre, ingrediente_unidad_medida, ingrediente_costo_por_unidad)
        ingredientes.append(ingrediente)
    pasos = []
    descripciones = []
    while True:
        paso = input("Ingrese el número del plato (o 'fin' para terminar): ")
        if paso.lower() == 'fin':
            break
        descripcion = input("Ingrese la descripción del plato: ")
        pasos.append(int(paso))
        descripciones.append(descripcion)
    receta = RecetaTextual(pasos, descripciones)
    comida = ComidaTextual(nombre, tipo_plato)
    comida.ingredientes = ingredientes
    comida.receta = receta
    return comida


comidas = []
comidas.append(ingresar_comida())
comidas.append(ingresar_comida())

mostrar_listado_comidas(comidas)


for comida in comidas:
    print("\nDetalles de la comida:")
    comida.mostrar_comida()