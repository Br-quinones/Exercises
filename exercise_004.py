"""
Has un programa que debe hacer lo siguiente:
Crear un diccionario vacío para guardar la información de un usuario.
Preguntarle al usuario su nombre, su edad y su hobby favorito.
Guardar cada una de esas respuestas en el diccionario. Las claves deben ser "nombre", "edad" y "hobby".
Finalmente, mostrar la información de una forma ordenada, accediendo a los valores a través de las claves del diccionario.
"""

import msvcrt
import sys
import os

data_center = {
    "name" : "",
    "age" : "",
    "hobby": "",
}

def see_menu():
    os.system("cls")

    print(" --- Utilize su teclado para elegir --- ")
    print("[1]. Introducir datos.")
    print("[2]. Observar datos.")
    print("[3]. Salir")

def see_quest():
    global data_center
    os.system("cls")

    print("--- introduzca su información ---")

    user_name = input("¿Cuál es tu nombre?: ")
    data_center["name"] = user_name
    user_age = input("¿Cuántos años tienes?: ")
    data_center["age"] = user_age
    user_hobby = input("¿Cuál es tu hobby?: ")
    data_center["hobby"] = user_hobby

    print("---------------------------------")

    print("Presione una tecla para volver.")
    msvcrt.getch()

def see_data():
    os.system("cls")

    print("--- Perfil de Usuario ---")
    print(f"Nombre: {data_center["name"]}")
    print(f"Edad: {data_center["age"]}")
    print(f"Hobby: {data_center["hobby"]}")
    print("-------------------------")

    print("Presione una tecla para volver.")
    msvcrt.getch()

while True:
    see_menu()

    key = msvcrt.getch().decode('latin-1')

    if key == "1":
        see_quest()
    elif key == "2":
        see_data()
    elif key == "3":
        sys.exit()

#26:06 minutos