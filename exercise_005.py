"""
has una función llamada es_contrasena_segura. Esta función recibirá una contraseña (como texto) y determinará si es lo suficientemente fuerte o no, devolviendo True (si es segura) o False (si no lo es).
Una contraseña se considera "segura" si cumple TODAS estas reglas a la vez:
1. Debe tener al menos 8 caracteres de longitud.
2. Debe contener al menos un número (0 al 9).
3. Debe contener al menos una letra mayúscula (A-Z).
En tu programa principal, pídele al usuario que ingrese una contraseña. Luego, llama a tu función para verificarla y finalmente dile al usuario si su contraseña es segura o no.
"""

import msvcrt
import os

def it_is_a_secure_password(password_attempt):
    def filter_00():
        comprobation = False

        if len(list(password_attempt)) >= 8:
            return True
        
        return comprobation

    def filter_01():
        comprobation = False

        for x in list(password_attempt):
            if x.isupper():
                comprobation = True
        
        return comprobation
    
    def filter_02():
        comprobation = False

        for x in list(password_attempt):
            if x.isdigit():
                comprobation = True
            
        return comprobation

    if filter_00() == True and filter_01() == True and filter_02() == True:
        return True
    else:
        return False
    
while True:
    os.system("cls")

    password = input("Introduce una contraseña para verificar su seguridad: ")

    print("---------------------------------")
    if it_is_a_secure_password(password) == True:
        print("Resultado: ¡Tu contraseña es segura!")
    elif it_is_a_secure_password(password) == False:
        print("Resultado: Tu contraseña NO es segura.")
    print("---------------------------------")

    msvcrt.getch()

#01:03:52 minutos