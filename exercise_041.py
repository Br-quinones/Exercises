#  Crea una funcion, que calcule el máximo común divisor (MCD) de dos números enteros
#  - Usar el algoritmo de euclides.
#  - No se pueden utilizar operaciones del lenguaje que
#    lo resuelvan directamente.

def euclidean_algorithm(number_01,number_02):
    remainder = number_01

    while True: 
        if remainder != 0:
            penultimate_remainder = remainder
        else:
            return penultimate_remainder

        if number_02 != 0:
            remainder = number_01 % number_02

        number_01 = number_02
        number_02 = remainder

print(f"De los números: 12 y 18 su MCD es: {euclidean_algorithm(12,18)}")
print(f"De los números: 20 y 5 su MCD es: {euclidean_algorithm(20,5)}")
print(f"De los números: 7 y 15 su MCD es: {euclidean_algorithm(7,15)}")
print(f"De los números: 99 y 11 su MCD es: {euclidean_algorithm(99,11)}")

#41:39 minutos