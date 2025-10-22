# Crea una clase llamada estudiantes 
# Agregale un __init__ para recibir el nombre
# Agregale un metodo para agregar nota 

class Students: 
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

# 1. Crear un estudiante
students_ana = Students("ana")

# 2. Añadir calificaciones usando el método
students_ana.add_grade(20)
students_ana.add_grade(10)
students_ana.add_grade(11)

# 3. Obtener el promedio usando el otro método
average_ana = students_ana.get_average()

# 4. Imprimimos el promedio del estudiante
print(f"Del estudiante: {students_ana.name} su promedio es: {average_ana}")

# 57 minutos