"""
Crearás una función que encuentre el número más grande dentro de una lista de números
"""

import msvcrt

number_list = [-8, 45, 87, 21, 99, 32, 50, 78, 100]

def find_maximum(list):
    max_value = number_list[0]
    for iterador in list:
        if iterador > max_value:
            max_value = iterador
    return max_value

print("--- Max valor de una lista ---")
print(f"Dada la lista: {number_list}")
print("-----------------------------")
print(f"El número mas grande es: {find_maximum(number_list)}")
print("-----------------------------")
print("Presione una tecla para salir.")
print("------------------------------")

msvcrt.getch()

#07:29 minutos