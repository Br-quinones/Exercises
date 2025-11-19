# Comprueba si un numero esta en una lista ordenada, usando la busqueda binaria. 
# Utiliza una funcion que devuelva un boleano
# No se puede usar el metodos in.

def number_to_look_for(ordered_list, number):
    while True:
        middle_position = int(len(ordered_list)) // 2
        middle_element = ordered_list[middle_position]

        if number == middle_element:
            return True
        
        elif number > middle_element:
            ordered_list = ordered_list[middle_position:]

        elif number < middle_element:
            ordered_list = ordered_list[:middle_position]

        # Comprobation 01
        if len(ordered_list) == 0:
            return False

user_ordered_list = [1,4,6,8,12,43,44,56,65,78,99,100,101,199,200,430]

print(number_to_look_for(user_ordered_list, 8))

# 53:50 