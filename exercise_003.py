"""
Has una función llamada calcular_factorial. Esta función debe hacer lo siguiente:

Calcular el factorial de ese número. El factorial es la multiplicación de todos los números enteros desde 1 hasta el número. Por ejemplo, el factorial de 5 es 120. 

Devolver (return) el resultado del cálculo. No debe imprimir nada dentro de la función.
"""

import os 
import msvcrt

def calculate_factorial(n):
    lista = []
    zero = 0
    for _ in range (n):
        consecutive_number = n - zero
        lista.append(consecutive_number)   
        zero += 1

    bottom_line = 1
    for number in lista:
        bottom_line = bottom_line * number

    return bottom_line

while True:
    os.system("cls")

    try:
        number_to_factorial = int(input("Escribe un número entero para calcular su factorial: "))
        print(f"El factorial de {number_to_factorial} es {calculate_factorial(number_to_factorial)}")
    except:
        print("Escriba un numero entero!")

    print("\n" + "Presione cualquier tecla para continuar")
    msvcrt.getch()

#1:20:30 minutos