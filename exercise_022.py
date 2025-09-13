# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#   las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

import msvcrt
import os

def if_this_is_an_anagram(word_01 , word_02):
    this_is_an_anagram = False

    if word_01 == word_02:
        this_is_an_anagram = False
    elif sorted(word_01) == sorted(word_02):
        this_is_an_anagram =  True
    
    return this_is_an_anagram

while True:
    os.system("cls")

    print("---- Detector de anagrama ----")
    user_word_01 = input("Introduzca una palabra: ").lower().lstrip().rstrip()
    user_word_02 = input("Introduzca otra palabra: ").lower().lstrip().rstrip()
    print("------------------------------")

    print(f"La validacion es: {if_this_is_an_anagram(user_word_01 , user_word_02)}")

    print("Presione una tecla para continuar")
    msvcrt.getch()

#29:59 minutos