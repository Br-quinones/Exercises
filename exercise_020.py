"""
Mejora el codigo del ejercicio 19 con estos cambios:
1. Falta la Condición de Derrota
2. Mostrar Letras Ya Usadas
3. Usa enumerate
4. Utiliza .join()
"""

import random
import msvcrt
import sys
import os

def press_continue(to_print):
    print("------------------------------")
    print(to_print)
    print("------------------------------")
    msvcrt.getch()

list_word = ["navidad","felicidad","dinero","francia","revolucion","cortina"]

the_word = random.choice(list_word)
words_used = []
final_list = []
lives = 6

for number in the_word:
    final_list.append("*")

while True:
    os.system("cls")

    print("       Juego el ahogado       ")
    print("------------------------------")
    print(f"VIDAS RESTANTES: {lives}")
    print("Palabra: " , " ".join(final_list))
    print("------------------------------")

    key = input("Introduzca una letra: ").lower().lstrip().rstrip()

    if key in words_used:
        press_continue("Letra ya utilizada")
    elif key in the_word:
        press_continue("Letra correcta.")
        for position,letter in enumerate(list(the_word)):
            if key == letter:
                final_list[position] = letter
                words_used.append(letter)
    elif key == " ":
        press_continue("No se aceptan espacios vacios.")
    elif key not in words_used:
        press_continue("Letra incorrecta.")
        lives -= 1

    if "*" not in final_list:
        os.system("cls")
        press_continue(f"Victoria, la palabra era: {the_word}.")
        sys.exit()
    if lives <= 0:
        os.system("cls")
        press_continue(f"Derrota, la palabra era: {the_word}")
        sys.exit()

#59:52 minutos