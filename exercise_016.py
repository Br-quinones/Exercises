"""
Refactoriza y desbugea el ejercicio anterior
"""

import msvcrt

numerical_list = [99, -2, 0, 12, 14, 23, 23, 34, 34, 99]

def second_largest_number(list_of_numbers):
    list_of_numbers = list(set(list_of_numbers)) #Factorizado

    ### Obtenemos el minimo valor posible
    first_min_value = list_of_numbers[0]
    for x in list_of_numbers:
        if x < first_min_value:
            first_min_value = x

    ### Con el minimo calculamos el maximo
    first_max_value = first_min_value
    for y in list_of_numbers:
        if y > first_max_value:
            first_max_value = y

    ### Con el maximo sacamos al segundo
    second_max_number = first_min_value
    for z in list_of_numbers:
        if z > second_max_number and z != first_max_value:
            second_max_number = z

    return second_max_number

print("------------------------------")
print(f"De la lista: {numerical_list}")
print("------------------------------")
print(f"El segundo número mas grande es: {second_largest_number(numerical_list)}")
print("------------------------------")
print("Presione una tecla para salir.")
msvcrt.getch()

#17:48 minutos