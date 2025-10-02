#  Crea una funcion, que calcule el máximo común divisor (MCD) de dos números enteros.
#  - No se pueden utilizar operaciones del lenguaje que
#    lo resuelvan directamente.

def greatest_common_divisor(number_01,number_02):
    divisors_01 = []
    for divider_01 in range(2,number_01+1):
        if number_01 % divider_01 == 0:
            divisors_01.append(divider_01)
    
    divisors_02 = []
    for divider_02 in range(2,number_02+1):
        if number_02 % divider_02 == 0:
            divisors_02.append(divider_02) 

    result_gcd = 0
    for result_01 in divisors_01:
        for result_02 in divisors_02:
            if result_01 == result_02:
                result_gcd = result_02

    return result_gcd

user_number_01 = 18
user_number_02 = 12

print(f"De los numeros {user_number_01} y {user_number_02} su maximo comun divisor es: {greatest_common_divisor(user_number_01,user_number_02)}")

#58:11