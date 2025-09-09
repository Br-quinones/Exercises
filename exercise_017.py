"""
Crea un programa que saque la secuencia de las potencias
"""

import os
import msvcrt

while True:
    os.system("cls")

    print("--- Calculadore de potencias en secuencia ---")

    #### Pedimos numero
    while True:
        user_exponent = input("Elija el numero del exponente: ")
        user_loop = input("Elija el numero de repiticiones: ")

        try:
            user_loop = int(user_loop)
            user_exponent = int(user_exponent)
            break
        except: 
            print("Por favor ingrese solo número enteros.")

    #### Imprimimos potencia
    print("------------------------")
    for base in range(user_loop + 1):
        print(f"{base} a la {user_exponent}: {base**user_exponent}")
    print("------------------------")

    print("Presione cualquier tecla para continuar.")
    msvcrt.getch()

#37:34 minutos