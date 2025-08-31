"""
Has un programa para encriptar y desencriptar mensajes. Usaremos una técnica muy antigua llamada "Cifrado César", que consiste en mover cada letra de un mensaje un número determinado de posiciones en el abecedario. Usa el % ; ord() ; chr()
"""

import msvcrt
import os

cesar_alfa = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "ñ": 15,
    "o": 16,
    "p": 17,
    "q": 18,
    "r": 19,
    "s": 20,
    "t": 21,
    "u": 22,
    "v": 23,
    "w": 24,
    "x": 25,
    "y": 26,
    "z": 27,
}

list_cesar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def codex_cesar(message , rotations):
    codex = ""

    for letter in message:
        if letter in list_cesar:
            codex += list_cesar[((cesar_alfa[letter])+( rotations-1))%27]
        else:
            codex += letter

    return codex

while True: 
    os.system("cls")

    print("--- Cifrado César ---")

    message = input("Introduce el mensaje que quieres encriptar: ").lower().lstrip().rstrip()

    try:
        rotations = int(input("Introduce el número de desplazamiento: "))
    except:
        print("Solo se aceptan numeros naturales en las rotaciones.")

    print("----------------------------------")
    try:
        print(f"Mensaje encriptado: {codex_cesar(message , rotations)}")
    except:
        print("Algo salio mal, intentelo de nuevo.")
    print("----------------------------------")

    print("Presione una tecla para reiniciar.")
    msvcrt.getch()

#2:12:08 minutos