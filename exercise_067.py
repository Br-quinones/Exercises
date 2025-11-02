#  Crea una función que sea capaz de encriptar y+ desencriptar texto
#  utilizando el algoritmo de encriptación de Karaca
#  (debes buscar información sobre él).

def karaca_encryption(text):
    reversed_text = text[::-1]

    vowel_to_number = list(reversed_text)
    for position,vowel in enumerate(reversed_text):
        if vowel in "AÁaá":
            vowel_to_number[position] = "0"
        elif vowel in "EÉeé":
            vowel_to_number[position] = "1"
        elif vowel in "IÍií":
            vowel_to_number[position] = "2"
        elif vowel in "OÓoó":
            vowel_to_number[position] = "3"
        elif vowel in "UÚuú":
            vowel_to_number[position] = "4"

    text_with_aca = ("".join(vowel_to_number)) + "aca"

    return text_with_aca

def karaca_decryption(text):
    text_without_aca = text[0:-3]

    number_to_vowel = list(text_without_aca)
    for position,vowel in enumerate(number_to_vowel):
        if vowel in "0":
            number_to_vowel[position] = "a"
        elif vowel in "1":
            number_to_vowel[position] = "e"
        elif vowel in "2":
            number_to_vowel[position] = "i"
        elif vowel in "3":
            number_to_vowel[position] = "o"
        elif vowel in "4":
            number_to_vowel[position] = "u"

    reversed_text = str("".join(number_to_vowel))
    reversed_text = reversed_text[::-1]

    return reversed_text


original_text = "En un lugar de la mancha de cuyo nombre no quisera acordarme"

encrypted_text = karaca_encryption(original_text)
decrypted_text = karaca_decryption(encrypted_text)

print("---------------- texto encriptado ---------------")
print(encrypted_text)
print("---------------- texto desencriptado ----------------")
print(decrypted_text)

# 40 minutos