"""
Escribir un programa que encuentre el segundo número más grande en una lista
"""

import msvcrt

numerical_list = [99, -2, 0, 12, 14, 23, 23, 34, 34]

def second_largest_number(list_of_numbers):
    list_of_numbers = list(set(list_of_numbers)) #Evitamos numeros repetidos

    first_max_value = list_of_numbers[0]  
    second_max_value = list_of_numbers[0]

    for x in list_of_numbers:
        if x > first_max_value:
            first_max_value = x

    for y in list_of_numbers:
        if y > second_max_value and y != first_max_value:
            second_max_value = y

    return second_max_value

print("------------------------------")
print(f"De la lista: {numerical_list}")
print("------------------------------")
print(f"El segundo número mas grande es: {second_largest_number(numerical_list)}")
print("------------------------------")
print("Presione una tecla para salir.")
msvcrt.getch()

#44:57 minutos