#  Escribe una función que calcule si un número dado es un número de Armstrong
#  (o también llamado narcisista).
#  Si no conoces qué es un número de Armstrong, debes buscar información
#  al respecto.

def this_is_an_armstrong_number(number):
    number_to_verify = 0
    for unit in str(number):
        number_to_verify += (int(unit)**len(str(number))) 
    
    return number_to_verify == number

number_01 = 99
number_02 = 143
number_03 = 153

print(f"El numero {number_01} da en el verificador de armstrong como: {this_is_an_armstrong_number(number_01)}.")
print(f"El numero {number_02} da en el verificador de armstrong como: {this_is_an_armstrong_number(number_02)}.")
print(f"El numero {number_03} da en el verificador de armstrong como: {this_is_an_armstrong_number(number_03)}.")

#10:05 minutos