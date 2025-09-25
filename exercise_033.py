# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee 
#     de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

def palindron_checker(text):
    text_invert = ""
    text_normal = ""

    for letter in text:
        if letter != " ":
            text_invert += letter.lower()
            text_normal = letter + text_normal.lower()

    if text_invert == text_normal:
        return True
    else:
        return False

user_text = "Ana lleva al oso la avellana"
print(f"El texto: {user_text} da como resultado '{palindron_checker(user_text)}' en palindromo.")

#12:58 minutos