"""
has a simulardor un cajero automático para una única cuenta bancaria. Toda la información de la cuenta se guardará en un diccionario.
Crea el diccionario: Al principio del programa, crea un diccionario llamado cuenta que contenga dos claves: "pin" (un string, ej: "1234") y "saldo" (un número con decimales, ej: 5000.0).
Verificar PIN: El programa debe empezar pidiendo al usuario que ingrese su PIN. Si el PIN es incorrecto, debe mostrar un mensaje de error y terminar. Si es correcto, debe mostrar el menú principal.
Crear el Menú: El menú debe funcionar dentro de un bucle y tener las siguientes opciones, cada una en su propia función:
1. Consultar Saldo: Muestra el saldo actual de la cuenta.
2. Depositar Dinero: Pregunta cuánto dinero depositar y lo suma al saldo actual.
3. Retirar Dinero: Pregunta cuánto dinero retirar. Importante: Debe comprobar si hay fondos suficientes. Si se intenta retirar más dinero del que hay en el saldo, debe mostrar un mensaje de "Fondos insuficientes".
4. Salir: Termina el programa.
"""

import msvcrt
import random
import sys
import os

bank_accounts = {
    "12345" : 0,
    "54321" : 0,
    "00000" : 0,
    "99999" : 0,
}

for pin in bank_accounts:
    number = float(random.randint(10,100) * 10)
    bank_accounts[pin] = number

while True:
    os.system("cls")

    print("----- Bienvenido al Cajero Automático -----")
    user_pin = input("Por favor, ingrese su PIN: ").rstrip().lstrip()
    print("-------------------------------------------")
    
    if user_pin in bank_accounts:
        print("Listo, usted accedió a su cuenta.")
        msvcrt.getch()
        break

    else:
        print("Lo siento, pero ese PIN no exite.")
        msvcrt.getch()
        pass

while True:
    os.system("cls")

    print("---- Menú Principal ----")
    print("1. Consultar Saldo      ")
    print("2. Depositar Dinero     ")
    print("3. Retirar Dinero       ")
    print("4. Salir                ")
    print("------------------------")

    key = msvcrt.getch().decode("latin-1")

    match key:
        case "1":
            os.system("cls")

            print("------------------------")
            print(f"Su saldo actual es: S/{bank_accounts[user_pin]}")
            print("------------------------")

            msvcrt.getch()
        
        case "2":
            os.system("cls")

            try:
                print("------------------------")
                print(f"Su saldo actual es: S/{bank_accounts[user_pin]}")
                add_balance= float(input(("¿Cuanto desea ingresar?: ")))
                
                bank_accounts[user_pin] += add_balance

                print("------------------------")
                print(f"Ingreo exitoso. Su nuevo saldo es: {bank_accounts[user_pin]}")
                print("------------------------")
            
            except:
                print("------------------------")
                print("Por favor ingrese un numero.")
                print("------------------------")

            msvcrt.getch()

        case "3":
            os.system("cls")
            
            try:
                print("------------------------")
                print(f"Su saldo actual es: S/{bank_accounts[user_pin]}")
                subtract_balance= float(input(("¿Cuanto desea retirar?: ")))
                
                if subtract_balance <= bank_accounts[user_pin]:
                    bank_accounts[user_pin] -= subtract_balance
                    print("------------------------")
                    print(f"Retiro exitoso. Su nuevo saldo es: {bank_accounts[user_pin]}")
                    print("------------------------")
                else:
                    print("------------------------")
                    print("Fondos insuficientes.")
                    print("------------------------")

            except:
                print("------------------------")
                print("Por favor ingrese un numero.")
                print("------------------------")

            msvcrt.getch()

        case "4":
            sys.exit()
        case _:
            print("Elija una tecla valida.")

#33:08