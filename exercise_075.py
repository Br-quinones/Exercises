# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def text_to_dict_with_len(text):
    text = "".join([letter for letter in text if letter not in [".", ",", ":", ";"]])
    return {word : len(word) for word in text.split()}

user_text = "En un lugar de la mancha de cuyo nombre no quisiera recordar no hace mucho tiempo que..."
print(text_to_dict_with_len(user_text))

# 25 minutes