"""
Crear una función que reciba una lista de diccionarios de estudiantes, calcule el promedio de cada uno, y devuelva la lista completa con los promedios añadidos.
"""

import msvcrt

student_note = [
    {"nombre": "Juan", "notas": [8, 7, 9, 10]},
    {"nombre": "Ana", "notas": [10, 9, 10, 9]},
    {"nombre": "Carlos", "notas": [6, 7, 5, 6]},
    {"nombre": "Sofia", "notas": []},
]

def average_calculator(estudent , data_center):
    zero = 0
    for data in data_center:
        if estudent in dict(data).values():
            if len(data_center[zero]["notas"]) != 0:
                result = sum(data_center[zero]["notas"])/len(data_center[zero]["notas"]) ; break
            else:
                result = "0.0"
        else:
            result =  "Error datos no encontrados"
        zero += 1
    return result 

list_of_students = ["Juan", "Ana", "Carlos", "Sofia"]

print("--- Promedios de la clase ---")

for names in list_of_students:
    number_list = 0
    print(f"Nombre: {names}")
    print(f"Notas: {student_note[number_list]["notas"]}")
    print(f"Promedio: {average_calculator(names , student_note)}")
    print("------------------------------")
    number_list += 1

print("Presione cualquier tecla para salir.")
msvcrt.getch()

#01:01:46 minutos