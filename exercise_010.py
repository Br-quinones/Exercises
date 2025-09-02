"""
Este reto no es sacado de Gemini 2.5 Pro. Sino que es el mismo de ayer solo que estaba vez lo hare como se deve, hoy en mi salon de clases por fin mi cerebro reacciono y se me prendio el foco, ahora con este nuevo conocimiento volvere a resolver el ejercicio.
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

def browser(word):
    position = 0
    word = str(word).lower().lstrip().rstrip()
    list_of_keys= ["nombre" , "telefono" , "email"]
    list_of_results = []

    for dictionary_lists in contactos: 
        for key in list_of_keys:
            if word in contactos[position][key].lower():
                list_of_results.append(contactos[position])
        position += 1

    list_of_values = []
    position = 0

    for y in list_of_results:
        diccionario = dict(list_of_results[position])
        for x in diccionario.values():
            list_of_values.append(x)
        position += 1

    final_list = []

    for x in list_of_values:
        if x not in final_list:
            final_list.append(x)

    return final_list

while True:
    os.system("cls")

    print("--- Buscador de contactos ---")
    search = input("¿A quien quieres buscar?: ")

    print("                                           ")
    print(f"--- Resultados de busqueda de {search} ---")
    print("                                           ")

    search_result = browser(search)
    list_keys = ["Nombre" , "Telefono" , "Email"]
    number_of_iterations = 0

    for data in search_result:
        if number_of_iterations == 3:
            print("---------------------------")
            number_of_iterations = 0
        
        print(f"{list_keys[number_of_iterations]}: {data}")

        number_of_iterations += 1

    msvcrt.getch()

    #01:10:27