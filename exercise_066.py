# Crea una función que reciba un texto y devuelva la vocal que se repite con mayor frecuencia.
# - Ten cuidado con algunos casos especiales.
# - Si no hay vocales, puede devolver una función vacía.
# - Se toma en cuenta el diccionario español
# - No usar librerias externas ni funciones del propio lenguaje que lo incluyan

def the_most_repeated_vowel(text):
    dict_vowels_numbers = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0,
    }

    for vowel in text:
        if vowel in "AÁaá":
            dict_vowels_numbers["a"] += 1
        if vowel in "EÉeé":
            dict_vowels_numbers["e"] += 1
        if vowel in "IÍií":
            dict_vowels_numbers["i"] += 1
        if vowel in "OÓoó":
            dict_vowels_numbers["o"] += 1
        if vowel in "UÚuú":
            dict_vowels_numbers["u"] += 1

    vowel_to_return = ""
    amount_of_vowel = 0

    print(dict_vowels_numbers)

    for vowel in dict_vowels_numbers:
        if dict_vowels_numbers[vowel] > amount_of_vowel:
            amount_of_vowel = dict_vowels_numbers[vowel] 
            vowel_to_return = vowel

        elif dict_vowels_numbers[vowel] == amount_of_vowel and dict_vowels_numbers[vowel] != 0:
            vowel_to_return = vowel_to_return + vowel

    return vowel_to_return

text_01 = "Ángel amaba a Érika. Ella le pidió un único favor que Íñigo y Óscar solo mirarían."
text_02 = "aaaaaeeeee"

print(the_most_repeated_vowel(text_01))
print(the_most_repeated_vowel(text_02))

#73 minutos