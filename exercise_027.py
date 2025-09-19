# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invert_string(word_to_invert):
    list_for_invert = list(word_to_invert)
    number_elements = len(word_to_invert) - 1
    for letter in word_to_invert:
        list_for_invert[number_elements] = letter
        number_elements -= 1

    inverted_word = "".join(list_for_invert)

    return inverted_word

print("--- Invertir palabra ---")
user_word = input("Introduzca una palabra: ")
print("------------------------")
print(f"La palabra invertida: {invert_string(user_word)}")

#36:20 minutos