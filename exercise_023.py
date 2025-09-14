# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.
# - No usar el .sorted()

import msvcrt
import os

def if_this_is_an_anagram(word_01 , word_02):
    alphabet = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "ñ" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    
    if word_01 == word_02 or len(word_01) != len(word_02):
        return False   
    
    dictionario_01 = dict(alphabet)
    for letter_01 in word_01:
        dictionario_01[letter_01] += 1
    dictionario_02 = dict(alphabet)
    for letter_02 in word_02:
        dictionario_02[letter_02] += 1

    return dictionario_01 == dictionario_02

while True:
    os.system("cls")

    print("--- Verificador de anagramas ---")
    user_word_01 = input("1. Introduzca una palabra: ").lower().lstrip().rstrip()
    user_word_02 = input("2. Introduzca una palabra: ").lower().lstrip().rstrip()
    print("--------------------------------")

    print(f"La verificacion es: {if_this_is_an_anagram(user_word_01 , user_word_02)}")
    msvcrt.getch()

#37:06 minutos