# Crea un sistema de dialogos de un arroba

if __name__ == "__main__":
    import keyboard
    keyboard.press_and_release("alt+enter")

    import time
    for _ in range(8):
        keyboard.press_and_release("ctrl+plus")
        time.sleep(0.01)

def dialogue(message):
    def generate_dialogue_ascii(message_01,message_02,message_03,message_04):
            print(f"██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
            print(f"                  █             ")
            print(f"  █████████████   █             ") 
            print(f"  █           █   █             ") 
            print(f"  █  ███████  █   █             ") 
            print(f"  █  █     █  █   █             ") 
            print(f"  █  █  ████  █   █ {message_01}") 
            print(f"  █  █  █  █  █   █ {message_02}")
            print(f"  █  █  █  █  █   █ {message_03}") 
            print(f"  █  █  ████  █   █ {message_04}") 
            print(f"  █  █        █   █             ") 
            print(f"  █  ██████████   █             ") 
            print(f"  █               █             ") 
            print(f"  █████████████   █             ")     
            print(f"                  █             ")

    text_01 = message[0:90]
    text_02 = message[90:180]
    text_03 = message[180:270]
    text_04 = message[270:360]

    if len(message) > 360:
        text_04 = f"  *--- Excediste el numero maximo de palabras: {len(message)} de 360 palabras ---*  "

    generate_dialogue_ascii(text_01,text_02,text_03,text_04)

# Nuestro variables para colocar diccionarios
dialogo = "Arthas: Aquellos que osen empuñar la hoja prohibida de la Agonía de Escarcha se verán investidos de una fuerza incalculable y perpetua, pues el pedestal en la fría cueva de Rasganorte proclama que quien la tome blandirá poder eterno; sin embargo, esta formidable bendición es una sentencia."

# Los \n son para crear un ambiente de dialogo
print("\n"*17)
dialogue(dialogo)

# Para que no se cierre el programa
input("")

# 110 minutos