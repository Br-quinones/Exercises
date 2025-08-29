"""
Crear un programa para gestionar las notas de una clase. La información se guardará en una lista principal llamada alumnos. Cada elemento de esta lista será un diccionario que representa a un solo alumno.
Cada diccionario de alumno debe tener dos claves:
"nombre": El nombre del alumno (un string).
"notas": Una lista con todas las notas de ese alumno (números).
Tu programa debe mostrar un menú con las siguientes opciones:
Agregar Alumno: Pide un nombre y lo añade a la lista de alumnos. El nuevo alumno empieza con una lista de notas vacía.
Agregar Nota: Pide el nombre de un alumno, busca a ese alumno en la lista, y luego le pide una nueva nota para añadir a su lista de notas.
Mostrar Promedios: Recorre la lista de todos los alumnos y muestra el nombre de cada uno, su lista de notas y su promedio. Si un alumno no tiene notas, debe indicarlo.
Salir: Termina el programa.
"""

import os 
import sys 
import msvcrt

diccionario = {}

def add_student():
    os.system("cls")

    print("----------------------------------")
    new_student = input("Nombre del nuevo alumno: ").lower().rstrip().lstrip()
    print("----------------------------------")
    print("Alumno agregado, presione una tecla para continuar")
    msvcrt.getch()

    return new_student

def add_score():
    global diccionario

    try:
        os.system("cls")

        print("----------------------------------")
        for_which_student = input("¿Para qué alumno?: ").lower().rstrip().lstrip()

        if for_which_student in diccionario:
            variable = float(input("Introduzca su nota: "))
            diccionario[for_which_student].append(variable)
            print("----------------------------------")
        else:
            print("----------------------------------")
            print("El nombre del alumno no esta registrado, intentelo de nuevo.")
            print("----------------------------------")
        
        print("Presione una tecla para continuar")
        msvcrt.getch()

    except:
        print("Porfavor introduzca un numero en la nota.")

def see_student():
    os.system("cls")

    print("--- Calificaciones de la Clase ---")
    for name in list(diccionario.keys()):
        print(f"-Alumno: {name}")

        print(f"Notas: {diccionario[name]}")

        if len(diccionario[name]) == 0:
            print("Promedio: 0")
        else:
            print(f"Promedio: {sum(diccionario[name]) / len(diccionario[name])}")

        print("----------------------------------")

    print("Presione una tecla para continuar")
    msvcrt.getch()

while True:
    os.system("cls")

    print("---- Sistema de Calificaciones ----")
    print("1. Agregar Alumno   ")
    print("2. Agregar Nota     ")
    print("3. Mostrar Promedios")
    print("4. Salir            ")
    print("----------------------------------")

    key = msvcrt.getch().decode("latin-1")

    if key == "1":
        diccionario[add_student()] = []
    elif key == "2":
        add_score()
    elif key == "3":
        see_student()
    elif key == "4":
        sys.exit()
    else:
        print("Valor incorrecto.")


#1:23:11 minutos