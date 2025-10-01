#  Crea una función que transforme grados Celsius en Fahrenheit
#  y viceversa.
#  - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#    y su unidad ("C" o "F").
#  - En caso contrario retornará un error.

def celsius_and_fahrenheit(degrees):
    number_of_degrees = ""
    for letter in degrees:
        if letter in ["0","1","2","3","4","5","6","7","8","9"]:
            number_of_degrees += letter

    if "°C" in degrees:
        return str((int(number_of_degrees) * (9/5)) + 32) + " °F"
    elif "°F" in degrees:
        return str((int(number_of_degrees) - 32) * 5/9) + " °C"
    else:
        return "Error, se deve agrega 'C' o 'F' en el argumento."

user_celsius = "50 °C"
user_fahrenheit = "50 °F"

print(f"De grados {user_celsius} tranformados da como resultado: {celsius_and_fahrenheit(user_celsius)}")
print(f"De grados {user_fahrenheit} tranformados da como resultado: {celsius_and_fahrenheit(user_fahrenheit)}")

#29:36 minutos