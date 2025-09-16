# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

import msvcrt

def is_this_number_prime(number):
    number = int(number)

    if number == 2 or number == 3 or number == 5 or number == 7 or number == 11:
        return True
    elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number % 11 != 0 and number != 1:
        return True
    
    return False

print("--- Numeros primos del 1 al 100 ---")
for number in range(1,101):
    if is_this_number_prime(number):
        print(number)
print("-----------------------------------")
msvcrt.getch()

# 24:17 minutos 