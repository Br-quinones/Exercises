#  Crea una función que reciba un String de cualquier tipo y se encargue de
#  poner en mayúscula la primera letra de cada palabra.
#  - No se pueden utilizar operaciones del lenguaje que
#    lo resuelvan directamente.

def capitalize_each_word(string):
    text_to_return = ""
    for position,letter in enumerate(string):
        if position == 0 or string[position - 1] == " ":
            text_to_return += letter.upper()
        else:
            text_to_return += letter

    return text_to_return

string_01 = "la escucha activa es fundamental para decodificar correctamente el mensaje del emisor y evitar malentendidos."
string_02 = "un lenguaje corporal abierto y relajado suele transmitir confianza y facilita la interacción interpersonal."
string_03 = "los medios digitales han transformado significativamente la velocidad y el alcance de la difusión de información."

print(" --- Convertir a mayuscula la primera letra de un palabra en un texto --- ")
print(f"Prueba 1: {capitalize_each_word(string_01)}")
print(f"Prueba 2: {capitalize_each_word(string_02)}")
print(f"Prueba 3: {capitalize_each_word(string_03)}")

#21:35