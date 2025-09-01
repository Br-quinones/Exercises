"""
Vamos a crear un pequeño buscador para una lista de contactos. El programa tendrá una lista de personas (con su nombre, teléfono y email) y permitirá al usuario encontrar a alguien por su nombre.
"""

import msvcrt
import os

contactos = [
    {"nombre": "Ana Lopez",
    "telefono": "987654321",
    "email": "ana.lopez@example.com"},

    {"nombre": "Juan Martinez",
    "telefono": "123456789",
    "email": "juan.martinez@example.com"},

    {"nombre": "Maria Garcia",
    "telefono": "555444333",
    "email": "maria.garcia@example.com"},

    {"nombre": "Carlos Rodriguez",
    "telefono": "111222333",
    "email": "carlos.r@example.com"},

    {"nombre": "Mariana Sanchez",
    "telefono": "999888777",
    "email": "mariana.s@example.com"},
]

def browser(word):  #No pasa nada con esta funcion
    zero = 0
    lista = ["nombre" , "telefono" , "email"]

    for _ in contactos: 
        for x in lista:
            if word in contactos[zero][x].lower(): #Un list() fue lo que no pude resolver en solitario
                print(f"{x}: {contactos[zero][x]}")
                print("---------------")
        zero += 1

while True:
    os.system("cls")

    print("--- Buscador de contactos ---")
    search = input("¿A quien quieres buscar?: ").lstrip().rstrip().lower()

    print("                                           ")
    print(f"--- Resultados de busqueda de {search} ---")

    browser(search)

    msvcrt.getch()

#01:41:24 minutos