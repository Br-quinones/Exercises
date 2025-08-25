"""
Crea un programa que funcione como una lista de compras digital. El programa debe mostrarle al usuario un menú con opciones y no debe detenerse hasta que el usuario elija "Salir".
"""

import msvcrt 
import time
import sys
import os 

def graphic_menu():
    os.system("cls")
    print("** Menú de Lista de Compras **")
    print("1. Agregar articulo")
    print("2. Eliminar articulo")
    print("3. Mostrar articulos")
    print("4. Salir")
    print("")

def option_add_item():
    global list_of_items

    os.system("cls")

    item = input("¿Qué artículo quieres agregar?: ")
    list_of_items.append(item)

    print("\n" + "Articulo agregado!")
    time.sleep(0.4)

def option_see_item():
    os.system("cls")

    number_of_iterations = 0

    print("--- Tu Lista ---" + "\n")

    for _ in list_of_items:
        print(f"- {list_of_items[number_of_iterations]}")
        number_of_iterations += 1

    print("\n" + "----------------")

    print("\n" + "Presione cualquier tecla para volver.")
    msvcrt.getch()

def option_delete_item():
    os.system("cls")

    delete = input("Escriba el item a eliminar: ")

    if delete in list_of_items:
        list_of_items.remove(delete)
        print("Articulo removido")
        time.sleep(0.4)
    else:
        print("No se removio nignun articulo")
        time.sleep(0.4)
    
def option_exit():
    print("\n" + "Adios!")
    time.sleep(0.4)
    sys.exit()
    
list_of_items = []

while True:
    graphic_menu()

    print("Elija una opción...")
    choice_menu = key = msvcrt.getch().decode('latin-1')
    
    if choice_menu == "1": #Agregar articulo
        option_add_item()
    elif choice_menu == "2": #Eliminar articulo
        option_delete_item()
    elif choice_menu == "3": #Mostrar articulo
        option_see_item()
    elif choice_menu == "4": #Salir
        option_exit()
    else:
        print("Ninguna opción seleccionada.")
        time.sleep(0.4)

# 1:06:43 minutos