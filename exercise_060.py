# Clase base Vehiculo:
# Atributos: marca, modelo, año
# Método __init__ para inicializar los atributos.
# Método informacion que devuelva una cadena con la información del vehículo.
# Clase Coche (hereda de Vehiculo):
# Atributo adicional: numero_puertas
# Sobrescribe el método informacion para incluir el número de puertas.
# Clase Motocicleta (hereda de Vehiculo):
# Atributo adicional: tipo_manillar (ej: "deportivo", "clásico")
# Sobrescribe el método informacion para incluir el tipo de manillar.
# Crea instancias y prueba el sistema:
# Instancia un coche y una motocicleta.
# Imprime la información de cada vehículo.

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def information(self):
        return f"Vehiculo marca {self.make}, modelo {self.model} del año {self.year}"
    
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def information(self):
        return f"Vehiculo marca {self.make}, modelo {self.model} del año {self.year} con {self.doors} puertas."

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, handlebar):
        super().__init__(make, model, year)
        self.handlebar = handlebar

    def information(self):
        return f"Vehiculo marca {self.make}, modelo {self.model} del año {self.year} con {self.handlebar} de manillar."

vehicle_01 = Car("Tesla","Cybertruck",2019,4)
print(vehicle_01.information())

vehicle_02 = Motorcycle("Honda","CB 125F",2023,"Tubular")
print(vehicle_02.information())

# 33 minutos