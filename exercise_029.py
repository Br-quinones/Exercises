#   Crea un programa que sea capaz de transformar texto natural a código morse

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'}


def convert_to_morse(text_to_morse):
    morser_to_return = ""
    for letter in text_to_morse:
        if letter in morse_code.keys():
            morser_to_return += morse_code[letter] + "/"
        elif letter == " ":
            morser_to_return += "/"
        else:
            morser_to_return += letter

    return morser_to_return

user_text = input("Introduzca un texto para convetir a morse: ").lower().lstrip().rstrip()
print(f"Su texto a morse es: {convert_to_morse(user_text)}")

#09:58 minutos 