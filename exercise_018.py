"""
Crea un sistema que ordene una lista de menor a mayor sin usar .short()
"""

import msvcrt

def sort_list(list_to_sort):
    def find_min_value():
        min_value = list_to_sort[0]
        for number in list_to_sort:
            if number <= min_value:
                min_value =  number

        return min_value
    
    new_list = []

    for x in range(len(list_to_sort)):
        min_value = find_min_value()

        new_list.append(min_value)
        list_to_sort.remove(min_value)

    return new_list

list_01 = [1,99,-4,0,-2,5,54,67,43,43,4,13,54,31,43,12,22,143,20,-4,-999]

print("-------------------------------")
print(f"De la lista: {list_01}")
print("-------------------------------")
print(f"Su orden es: {sort_list(list_01)}")
print("-------------------------------")
print("Presione una tecla para salir.")
msvcrt.getch()
        

#33:34 minutos