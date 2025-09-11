"""
Crea el juego del ahogado
"""

import random
import msvcrt
import time
import sys
import os

def verification(checklist):
    if "-" not in checklist: #Verificiacion
        os.system("cls")
        time.sleep(0.3) #Encaso que el jugador aprete demasiado rapido
        print("Victoria para el jugador. Pulse una tecla para salir")
        msvcrt.getch()
        sys.exit()

list_words = ["serpiente", "elefante", "jirafa", "pinguino", "cocodrilo", "castillo", "television", "computadora", "bicicleta", "halloween", "carnaval", "chocolate", "manzana", "naranja", "platano", "zanahoria", "escuela", "ciudad", "pueblo", "desierto", "volcan", "tristeza", "felicidad", "realidad", "historia", "estrella", "amarillo", "morado", "blanco", "marron", "escribir", "escuchar", "trabajar", "rapido", "fuerte", "dificil", "caliente", "viejo", "bonito", "abecedario", "aeropuerto", "aniversario", "apartamento", "astronauta", "biblioteca", "bicicleta", "carretera", "celebracion", "cementerio", "computadora", "congelador", "conversacion", "diccionario", "electricidad", "estacionamiento", "fantasma", "fotografia", "helicoptero", "imaginacion", "inteligencia", "kilometro", "laboratorio", "misterioso", "naturaleza", "navegacion", "ordenador", "paracaidas", "perpendicular", "refrigerador", "satisfaccion", "submarino", "supermercado", "termometro", "trabajador", "universidad"]

the_word = random.choice(list_words)

script_list = []
for _ in the_word:
    script_list.append("-")

while True:
    os.system("cls") #Limpiando pantalla

    print(script_list) #mostrando la lista de guiones 

    verification(script_list) #Verificacion

    letter = input("Introduzca una letra: ").lstrip().rstrip().lower() #Pedir letra

    if letter in the_word:
        position = 0
        for x in the_word:
            if letter == x:
                script_list[position] = letter
            position += 1
        print("Letra correta.")
    else:
        print("Letra incorrecta.")

    msvcrt.getch()

#40:28 minutos