#Crea un programa se encargue de transformar un número
#decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def convert_decimal_to_binary(decimal_number):
    number_list = [decimal_number]

    number_to_add = decimal_number
    while number_to_add > 0:
        number_to_add = int(number_to_add / 2)
        number_list.append(number_to_add)

    numbers_no_inverter = ""
    for number in number_list:
        if number % 2 == 0:
            numbers_no_inverter += "0"
        elif number % 2 == 1:
            numbers_no_inverter += "1"

    number_to_return = numbers_no_inverter[::-1]

    return int(number_to_return)

user_number = int(input("Introduzca un numero decimal: "))
print(f"El numero en binario es: {convert_decimal_to_binary(user_number)}")

#34:04 minutos