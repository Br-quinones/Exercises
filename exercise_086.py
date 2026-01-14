# Dado un array de enteros ordenado y sin repetidos,
# crea una función que calcule y retorne todos los que faltan entre
# el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.

def missing_from_least_to_greatest(the_list: list):
    # Checking empty
    if len(the_list) == 0:
        raise ValueError("Invalid: empty list")

    # checking repetitions
    if len(the_list) != len(set(the_list)):
        raise ValueError ("Invalid: repetide numbers")

    # Checking order
    if the_list != sorted(the_list):
        raise ValueError("Invalid: unordered list")

    # Get range
    min_number_range = the_list[0] + 1
    max_number_range = the_list[-1]

    # Operations
    list_to_return = []
    for number in range(min_number_range,max_number_range):
        if number not in the_list:
            list_to_return.append(number)
            
    return list_to_return

user_list = []
print(missing_from_least_to_greatest(user_list)) 